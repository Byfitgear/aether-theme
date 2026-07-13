from sqlalchemy import Column, String, DateTime, Boolean, Enum as SAEnum, JSON
from sqlalchemy.sql import func
import enum

from ..core.database import Base


class PlanType(str, enum.Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)  # Clerk user ID
    email = Column(String(255), unique=True, nullable=False, index=True)
    name = Column(String(255))
    avatar_url = Column(String(512))
    plan = Column(SAEnum(PlanType), default=PlanType.FREE, nullable=False)
    clerk_id = Column(String(100), unique=True, nullable=False)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    metadata_ = Column("metadata", JSON, default=dict)
