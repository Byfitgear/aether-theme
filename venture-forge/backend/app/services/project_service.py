"""项目管理服务"""
import uuid
from typing import Optional, List
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from ..models.project import Project
from ..schemas.project import ProjectCreate, ProjectResponse


class ProjectService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, data: ProjectCreate) -> Project:
        project = Project(
            id=str(uuid.uuid4()),
            opportunity_id=data.opportunity_id,
            user_id=data.user_id,
            name=data.name,
            tagline=data.tagline,
            description=data.description,
            tech_stack=data.tech_stack or [],
            status="generated",
        )
        self.db.add(project)
        await self.db.commit()
        await self.db.refresh(project)
        return project
    
    async def get_by_id(self, project_id: str) -> Optional[Project]:
        result = await self.db.execute(select(Project).where(Project.id == project_id))
        return result.scalar_one_or_none()
    
    async def list_by_user(self, user_id: str, limit: int = 20) -> List[Project]:
        result = await self.db.execute(
            select(Project)
            .where(Project.user_id == user_id)
            .order_by(desc(Project.created_at))
            .limit(limit)
        )
        return list(result.scalars().all())
    
    async def deploy(self, project_id: str, deploy_url: str) -> Optional[Project]:
        project = await self.get_by_id(project_id)
        if project:
            project.deploy_url = deploy_url
            project.status = "deployed"
            await self.db.commit()
            await self.db.refresh(project)
        return project
