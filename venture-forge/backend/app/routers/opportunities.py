"""机会管理API路由"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_db
from ..services.opportunity_service import OpportunityService
from ..schemas.opportunity import OpportunityCreate, OpportunityResponse

router = APIRouter(prefix="/api/v1/opportunities", tags=["opportunities"])


@router.post("/", response_model=OpportunityResponse)
async def create_opportunity(
    data: OpportunityCreate,
    db: AsyncSession = Depends(get_db),
):
    service = OpportunityService(db)
    opp = await service.create(data)
    return opp


@router.get("/", response_model=list[OpportunityResponse])
async def list_opportunities(
    limit: int = 50,
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
):
    service = OpportunityService(db)
    opps = await service.list_all(limit=limit, offset=offset)
    return opps


@router.get("/{opportunity_id}", response_model=OpportunityResponse)
async def get_opportunity(
    opportunity_id: str,
    db: AsyncSession = Depends(get_db),
):
    service = OpportunityService(db)
    opp = await service.get_by_id(opportunity_id)
    if not opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return opp


@router.patch("/{opportunity_id}/status")
async def update_opportunity_status(
    opportunity_id: str,
    status: str,
    db: AsyncSession = Depends(get_db),
):
    service = OpportunityService(db)
    opp = await service.update_status(opportunity_id, status)
    if not opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return {"message": f"Status updated to {status}", "opportunity": opp}
