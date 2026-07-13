"""市场扫描服务 — 协调Agent执行扫描"""
import logging
from typing import Optional

from ..agents.market_scanner import MarketScannerAgent
from ..agents.opportunity_scorer import OpportunityScorerAgent

logger = logging.getLogger(__name__)


class ScannerService:
    """市场扫描编排服务"""
    
    def __init__(self):
        self.scanner = MarketScannerAgent()
        self.scorer = OpportunityScorerAgent()
    
    async def run_full_scan(self) -> dict:
        """执行完整扫描→评分流程"""
        logger.info("Starting full market scan...")
        
        # Step 1: 扫描所有平台
        raw_findings = await self.scanner.scan_all_platforms()
        logger.info(f"Found {len(raw_findings)} raw findings")
        
        # Step 2: 提取痛点
        pain_points = self.scanner.extract_pain_points(raw_findings)
        logger.info(f"Extracted {len(pain_points)} pain points")
        
        # Step 3: 评分
        scored_opportunities = []
        for pp in pain_points[:20]:  # Score top 20
            score = await self.scorer.score_opportunity(pp)
            scored_opportunities.append(score)
        
        # Step 4: 筛选高分机会
        high_value = self.scorer.filter_high_value(scored_opportunities, threshold=80)
        
        return {
            "total_findings": len(raw_findings),
            "pain_points_extracted": len(pain_points),
            "opportunities_scored": len(scored_opportunities),
            "high_value_opportunities": len(high_value),
            "top_opportunities": sorted(
                scored_opportunities,
                key=lambda x: x.get("total_score", 0),
                reverse=True
            )[:10],
        }
