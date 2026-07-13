"""指标管理API路由"""
import uuid
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from ..core.database import get_db
from ..models.metric import Metric

router = APIRouter(prefix="/api/v1/metrics", tags=["metrics"])


@router.post("/")
async def record_metric(
    project_id: str,
    metric_name: str,
    value: float,
    period_start: str = None,
    period_end: str = None,
    metadata_: dict = {},
    db: AsyncSession = Depends(get_db),
):
    """记录一个新的增长指标"""
    metric = Metric(
        id=str(uuid.uuid4()),
        project_id=project_id,
        metric_name=metric_name,
        value=value,
        period_start=datetime.fromisoformat(period_start) if period_start else None,
        period_end=datetime.fromisoformat(period_end) if period_end else None,
        metadata_=metadata_,
    )
    db.add(metric)
    await db.commit()
    await db.refresh(metric)
    return {"message": "Metric recorded", "metric_id": metric.id}


@router.get("/project/{project_id}")
async def get_project_metrics(
    project_id: str,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
):
    """获取项目的所有指标"""
    result = await db.execute(
        select(Metric)
        .where(Metric.project_id == project_id)
        .order_by(desc(Metric.created_at))
        .limit(limit)
    )
    metrics = result.scalars().all()
    
    return [
        {
            "id": m.id,
            "metric_name": m.metric_name,
            "value": m.value,
            "period_start": m.period_start.isoformat() if m.period_start else None,
            "period_end": m.period_end.isoformat() if m.period_end else None,
            "created_at": m.created_at.isoformat() if m.created_at else None,
        }
        for m in metrics
    ]


@router.get("/dashboard/project/{project_id}")
async def get_dashboard_stats(
    project_id: str,
    db: AsyncSession = Depends(get_db),
):
    """获取仪表盘汇总统计"""
    result = await db.execute(
        select(Metric).where(Metric.project_id == project_id)
    )
    all_metrics = result.scalars().all()
    
    # Group by metric_name, get latest value
    latest = {}
    for m in all_metrics:
        key = m.metric_name
        if key not in latest or (m.created_at and latest[key].created_at < m.created_at):
            latest[key] = m
    
    return {
        "project_id": project_id,
        "latest_values": {
            name: {"value": m.value, "recorded_at": m.created_at.isoformat() if m.created_at else None}
            for name, m in latest.items()
        },
        "total_records": len(all_metrics),
    }
