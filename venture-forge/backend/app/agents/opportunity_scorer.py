"""机会评分Agent — 量化市场机会"""
import json
import logging
from typing import Optional
from datetime import datetime

from ..core.config import get_settings

logger = logging.getLogger(__name__)


class OpportunityScorerAgent:
    """市场机会评分引擎"""
    
    WEIGHTS = {
        "market_size": 0.30,    # TAM/SAM/SOM
        "competition": 0.20,    # 竞争强度（越低越好）
        "dev_difficulty": 0.15, # 开发难度（越低越好）
        "ai_replaceability": 0.20,  # AI替代能力
        "profitability": 0.15,  # 盈利能力
    }
    
    async def score_opportunity(self, pain_point: dict) -> dict:
        """对单个痛点进行完整商业评分"""
        # 1. LLM驱动的深度分析
        analysis = await self._deep_analyze(pain_point)
        
        if not analysis:
            # 降级：基于规则评分
            analysis = self._rule_based_score(pain_point)
        
        # 2. 计算加权总分
        total_score = sum(
            category["score"] * weight
            for category, weight in zip(
                [analysis.get("market_size", {}),
                 analysis.get("competition", {}),
                 analysis.get("dev_difficulty", {}),
                 analysis.get("ai_replaceability", {}),
                 analysis.get("profitability", {})],
                self.WEIGHTS.values()
            )
        )
        
        result = {
            **analysis,
            "total_score": round(total_score, 2),
            "pain_point": pain_point,
            "scored_at": datetime.utcnow().isoformat(),
            "meets_threshold": total_score >= 80,
        }
        
        return result
    
    async def _deep_analyze(self, pain_point: dict) -> Optional[dict]:
        """使用LLM进行深度商业分析"""
        try:
            from langchain_openai import ChatOpenAI
            
            llm = ChatOpenAI(model="gpt-4o", temperature=0.3)
            
            prompt = f"""
            Analyze this market opportunity and provide a detailed business evaluation.
            
            Pain Point: {pain_point.get('raw_title', '')}
            Platform: {pain_point.get('platform', '')}
            Category: {pain_point.get('category', '')}
            Signal Strength: {pain_point.get('signal', 0)}
            
            Return ONLY valid JSON (no markdown, no backticks):
            {{
                "market_size": {{
                    "score": <0-10>,
                    "tam": "$X.XB",
                    "sam": "$X.XB",
                    "som": "$X.XM",
                    "growth_rate": "<%>"
                }},
                "competition": {{
                    "score": <0-10>,
                    "main_competitors": ["Name1", "Name2"],
                    "barrier_to_entry": "<high|medium|low>",
                    "network_effect_potential": <boolean>
                }},
                "dev_difficulty": {{
                    "score": <0-10>,
                    "estimated_dev_time": "<weeks>",
                    "required_skills": ["skill1", "skill2"],
                    "infrastructure_cost": "<low|medium|high>"
                }},
                "ai_replaceability": {{
                    "score": <0-10>,
                    "ai_advantage": "<how AI creates moat>",
                    "data_network_effect": <boolean>
                }},
                "profitability": {{
                    "score": <0-10>,
                    "cac_estimate": "$XX",
                    "ltv_estimate": "$XXX",
                    "gross_margin": "<XX>%",
                    "pricing_model": "<freemium|subscription|usage>"
                }}
            }}
            """
            
            response = llm.invoke(prompt)
            content = response.content.strip()
            
            # Clean up potential markdown formatting
            if content.startswith("```"):
                content = "\n".join(
                    line for line in content.split("\n")[1:]
                    if not line.strip().startswith("```")
                )
            
            return json.loads(content)
            
        except Exception as e:
            logger.error(f"LLM analysis failed: {e}")
            return None
    
    def _rule_based_score(self, pain_point: dict) -> dict:
        """降级：基于规则的快速评分"""
        signal = pain_point.get("signal", 2)
        
        return {
            "market_size": {"score": min(signal * 2, 10), "tam": "$10B+", "sam": "$2B", "som": "$100M"},
            "competition": {"score": 7, "main_competitors": [], "barrier_to_entry": "medium"},
            "dev_difficulty": {"score": 5, "estimated_dev_time": "4 weeks"},
            "ai_replaceability": {"score": min(signal * 1.5, 10)},
            "profitability": {"score": 7, "cac_estimate": "$15", "ltv_estimate": "$600", "gross_margin": "80%"},
        }
    
    def filter_high_value(self, scored_opportunities: list[dict], threshold: float = 80) -> list[dict]:
        """筛选高分机会"""
        return [op for op in scored_opportunities if op.get("total_score", 0) >= threshold]
