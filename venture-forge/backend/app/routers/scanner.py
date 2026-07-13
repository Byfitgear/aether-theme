"""市场扫描API路由 — 触发扫描和获取结果"""
import logging
from typing import List, Dict, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_db
from ..services.scanner_service import ScannerService
from ..models.opportunity import Opportunity

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/scanner", tags=["scanner"])


@router.post("/run")
async def trigger_scan(db: AsyncSession = Depends(get_db)):
    """触发完整市场扫描"""
    service = ScannerService()
    
    try:
        result = await service.run_full_scan()
        
        # 保存高分机会到数据库
        for opp_data in result.get("top_opportunities", []):
            pain = opp_data.get("pain_point", {})
            score_info = opp_data
        
            existing = await db.execute(
                Opportunity.__table__.select().where(
                    Opportunity.title == pain.get("raw_title", "")
                ).limit(1)
            )
            if not existing.scalar_one_or_none():
                from ..services.opportunity_service import OpportunityService
                svc = OpportunityService(db)
                await svc.create(OpportunityCreate(
                    title=pain.get("raw_title", ""),
                    description=f"Discovered via {pain.get('platform', 'unknown')} scan",
                    source_platform=pain.get("platform", "unknown"),
                    target_persona={"score": score_info.get("total_score")},
                ))
        
        await db.commit()
        
        return {
            "status": "completed",
            "findings": result,
        }
    except Exception as e:
        logger.error(f"Scan failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/results")
async def get_scan_results(db: AsyncSession = Depends(get_db)):
    """获取最近的扫描结果"""
    from sqlalchemy import select, desc
    result = await db.execute(
        select(Opportunity)
        .order_by(desc(Opportunity.created_at))
        .limit(20)
    )
    opportunities = result.scalars().all()
    
    return [
        {
            "id": o.id,
            "title": o.title,
            "source_platform": o.source_platform,
            "total_score": o.total_score or 0,
            "status": o.status,
            "created_at": o.created_at.isoformat() if o.created_at else None,
        }
        for o in opportunities
    ]
