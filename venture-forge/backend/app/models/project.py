from sqlalchemy import Column, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..core.database import Base


class Project(Base):
    """生成的MVP项目"""
    __tablename__ = "projects"

    id = Column(String(36), primary_key=True)
    opportunity_id = Column(String(36), ForeignKey("opportunities.id"), nullable=False)
    user_id = Column(String(36), nullable=False, index=True)
    
    name = Column(String(255), nullable=False)
    tagline = Column(String(500))
    description = Column(Text)
    
    # 生成的项目结构
    project_structure = Column(JSON, default=dict)
    tech_stack = Column(JSON, default=list)
    
    # 状态
    status = Column(String(20), default="generated")  # generated, building, deployed
    deploy_url = Column(String(500))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    opportunity = relationship("Opportunity")
