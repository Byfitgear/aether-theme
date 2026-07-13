from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any


class MetricCreate(BaseModel):
    project_id: str
    metric_name: str
    value: float
    period_start: Optional[datetime] = None
    period_end: Optional[datetime] = None
    metadata_: Optional[Dict[str, Any]] = {}


class MetricResponse(BaseModel):
    id: str
    project_id: str
    metric_name: str
    value: float
    period_start: Optional[datetime]
    period_end: Optional[datetime]
    created_at: datetime

    model_config = {"from_attributes": True}
