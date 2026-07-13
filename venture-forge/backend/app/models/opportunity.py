from sqlalchemy import Column, String, Text, Float, Integer, DateTime, JSON
from sqlalchemy.sql import func

from ..core.database import Base


class Opportunity(Base):
    """市场机会数据模型"""
    __tablename__ = "opportunities"

    id = Column(String(36), primary_key=True)
    title = Column(String(500), nullable=False, index=True)
    description = Column(Text, nullable=False)
    source_platform = Column(String(50), nullable=False)  # reddit, hackernews, etc
    source_url = Column(String(1000))
    
    # 评分字段
    pain_frequency = Column(Integer)  # 1-5
    market_size_score = Column(Float)
    competition_score = Column(Float)
    ai_difficulty = Column(Float)
    commercial_value = Column(Float)
    total_score = Column(Float)
    
    # 用户画像
    target_persona = Column(JSON, default=dict)
    
    # 市场分析
    tam = Column(String(100))
    sam = Column(String(100))
    som = Column(String(100))
    cac_estimate = Column(String(50))
    ltv_estimate = Column(String(50))
    
    # 状态
    status = Column(String(20), default="discovered")  # discovered, validated, building, launched
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    validated_at = Column(DateTime(timezone=True))
