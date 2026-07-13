"""机会管理服务"""
import uuid
from typing import Optional, List
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from ..models.opportunity import Opportunity
from ..schemas.opportunity import OpportunityCreate, OpportunityResponse


class OpportunityService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, data: OpportunityCreate) -> Opportunity:
        opp = Opportunity(
            id=str(uuid.uuid4()),
            title=data.title,
            description=data.description,
            source_platform=data.source_platform,
            source_url=data.source_url,
            target_persona=data.target_persona,
            status="discovered",
        )
        self.db.add(opp)
        await self.db.commit()
        await self.db.refresh(opp)
        return opp
    
    async def get_by_id(self, opp_id: str) -> Optional[Opportunity]:
        result = await self.db.execute(select(Opportunity).where(Opportunity.id == opp_id))
        return result.scalar_one_or_none()
    
    async def list_all(self, limit: int = 50, offset: int = 0) -> List[Opportunity]:
        result = await self.db.execute(
            select(Opportunity)
            .order_by(desc(Opportunity.created_at))
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())
    
    async def update_status(self, opp_id: str, status: str) -> Optional[Opportunity]:
        opp = await self.get_by_id(opp_id)
        if opp:
            opp.status = status
            if status == "validated":
                opp.validated_at = datetime.utcnow()
            await self.db.commit()
            await self.db.refresh(opp)
        return opp
