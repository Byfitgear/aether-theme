from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any


class OpportunityCreate(BaseModel):
    title: str
    description: str
    source_platform: str
    source_url: Optional[str] = None
    target_persona: Optional[Dict[str, Any]] = {}


class OpportunityScore(BaseModel):
    pain_frequency: int  # 1-5
    market_size_score: float
    competition_score: float
    ai_difficulty: float
    commercial_value: float
    total_score: float
    tam: Optional[str] = None
    sam: Optional[str] = None
    som: Optional[str] = None
    cac_estimate: Optional[str] = None
    ltv_estimate: Optional[str] = None


class OpportunityResponse(BaseModel):
    id: str
    title: str
    description: str
    source_platform: str
    total_score: float
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}
