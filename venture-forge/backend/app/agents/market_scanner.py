"""市场扫描Agent — 自动发现市场机会"""
import json
import logging
from typing import Optional
from datetime import datetime

import httpx

from ..core.config import get_settings

logger = logging.getLogger(__name__)


class MarketScannerAgent:
    """多源市场扫描Agent"""
    
    def __init__(self):
        self.settings = get_settings()
        self.platforms = {
            "reddit": {"base_url": "https://www.reddit.com/r/", "subreddits": ["startups", "entrepreneur", "SaaS", "findapartner"]},
            "hackernews": {"api": "https://hacker-news.firebaseio.com/v0"},
            "producthunt": {"api": "https://api.producthunt.com/v2/api/graphql"},
        }
    
    async def scan_all_platforms(self) -> list[dict]:
        """扫描所有数据源，返回原始痛点列表"""
        results = []
        
        # 并行扫描各平台
        tasks = [
            self._scan_reddit(),
            self._scan_hackernews(),
            self._simulate_product_hunt(),
        ]
        
        for task in tasks:
            try:
                findings = await task
                results.extend(findings)
            except Exception as e:
                logger.error(f"Scan failed: {e}")
        
        return results
    
    async def _scan_reddit(self) -> list[dict]:
        """扫描Reddit热门帖子中的抱怨"""
        findings = []
        async with httpx.AsyncClient(timeout=10.0) as client:
            for sub in self.platforms["reddit"]["subreddits"]:
                try:
                    resp = await client.get(
                        f"https://www.reddit.com/r/{sub}/hot.json?limit=25",
                        headers={"User-Agent": "VentureForge/1.0"}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        for post in data.get("data", {}).get("children", []):
                            title = post["data"].get("title", "")
                            score = post["data"].get("score", 0)
                            num_comments = post["data"].get("num_comments", 0)
                            
                            # 关键词匹配：高抱怨信号
                            complaint_keywords = [
                                "frustrated", "hate", "annoying", "why doesn't",
                                "wish there was", "so hard", "too expensive",
                                "takes too long", "manual", "tedious",
                                "complicated", "confusing", "broken",
                            ]
                            
                            if any(kw in title.lower() for kw in complaint_keywords) or score > 500:
                                findings.append({
                                    "platform": "reddit",
                                    "title": title,
                                    "score": score,
                                    "comments": num_comments,
                                    "url": f"https://reddit.com{post['data'].get('permalink', '')}",
                                    "subreddit": sub,
                                    "signal_strength": min(score / 100, 5),
                                })
                except Exception as e:
                    logger.warning(f"Reddit scan failed for r/{sub}: {e}")
        
        return findings[:20]  # Top 20
    
    async def _scan_hackernews(self) -> list[dict]:
        """扫描Hacker News"""
        findings = []
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                # 最新热门
                resp = await client.get(
                    "https://hacker-news.firebaseio.com/v0/topstories.json"
                )
                top_ids = resp.json()[:30]
                
                for item_id in top_ids:
                    resp2 = await client.get(
                        f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
                    )
                    item = resp2.json()
                    if item and item.get("score", 0) > 50:
                        title = item.get("title", "")
                        complaint_keywords = [
                            "would love if", "why isn't", "missing",
                            "alternative to", "better than", "pain point",
                        ]
                        if any(kw in title.lower() for kw in complaint_keywords):
                            findings.append({
                                "platform": "hackernews",
                                "title": title,
                                "score": item.get("score", 0),
                                "url": item.get("url", f"https://hn.algolia.com/?q={item_id}"),
                                "signal_strength": min(item.get("score", 0) / 50, 5),
                            })
            except Exception as e:
                logger.warning(f"HN scan failed: {e}")
        
        return findings[:10]
    
    async def _simulate_product_hunt(self) -> list[dict]:
        """模拟Product Hunt洞察（实际应调用API）"""
        # 基于公开数据的模拟发现
        return [
            {
                "platform": "producthunt",
                "title": "AI tools are too fragmented — founders need one unified builder",
                "signal_strength": 4.5,
                "category": "AI Developer Tools",
                "trend": "rising",
            },
            {
                "platform": "producthunt",
                "title": "No-code builders can't handle complex business logic",
                "signal_strength": 4.0,
                "category": "No-Code",
                "trend": "stable",
            },
        ]
    
    def extract_pain_points(self, raw_findings: list[dict]) -> list[dict]:
        """从原始发现中提取痛点"""
        pain_points = []
        for finding in raw_findings:
            # 使用OpenAI提取结构化痛点
            if self.settings.OPENAI_API_KEY:
                pain_point = self._extract_with_llm(finding)
            else:
                # 降级：基于规则的提取
                pain_point = self._rule_based_extract(finding)
            
            if pain_point:
                pain_points.append(pain_point)
        
        return sorted(pain_points, key=lambda x: x.get("signal", 0), reverse=True)
    
    def _rule_based_extract(self, finding: dict) -> Optional[dict]:
        """基于规则的痛点提取"""
        return {
            "raw_title": finding.get("title", ""),
            "platform": finding.get("platform", "unknown"),
            "signal": finding.get("signal_strength", 0),
            "url": finding.get("url", ""),
            "category": self._categorize(finding.get("title", "")),
        }
    
    def _categorize(self, text: str) -> str:
        """对痛点进行分类"""
        categories = {
            "dev tool": ["developer", "tool", "code", "build"],
            "time saver": ["manual", "tedious", "takes too long", "slow"],
            "cost reduction": ["expensive", "price", "cost", "budget"],
            "complexity": ["complicated", "complex", "hard", "confusing"],
        }
        text_lower = text.lower()
        for cat, keywords in categories.items():
            if any(kw in text_lower for kw in keywords):
                return cat
        return "general"
    
    def _extract_with_llm(self, finding: dict) -> Optional[dict]:
        """使用LLM提取结构化痛点"""
        try:
            from langchain_openai import ChatOpenAI
            
            llm = ChatOpenAI(model="gpt-4o", temperature=0)
            prompt = f"""
            Analyze this user feedback and extract a structured pain point.
            
            Title: {finding.get('title', '')}
            Platform: {finding.get('platform', '')}
            Signal Strength: {finding.get('signal_strength', 0)}
            
            Return JSON only:
            {{
                "raw_title": "...",
                "platform": "...",
                "signal": <number 0-5>,
                "url": "...",
                "category": "<dev tool|time saver|cost reduction|complexity|other>"
            }}
            """
            response = llm.invoke(prompt)
            return json.loads(response.content)
        except Exception as e:
            logger.error(f"LLM extraction failed: {e}")
            return None
