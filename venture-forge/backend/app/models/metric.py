from sqlalchemy import Column, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func

from ..core.database import Base


class Metric(Base):
    """增长指标追踪"""
    __tablename__ = "metrics"

    id = Column(String(36), primary_key=True)
    project_id = Column(String(36), ForeignKey("projects.id"), nullable=False)
    
    metric_name = Column(String(100), nullable=False)  # retention, conversion, cac, ltv, mau, nps
    value = Column(Float)
    period_start = Column(DateTime(timezone=True))
    period_end = Column(DateTime(timezone=True))
    metadata_ = Column("metadata", JSON, default=dict)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
