from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any, List


class ProjectCreate(BaseModel):
    opportunity_id: str
    user_id: str
    name: str
    tagline: Optional[str] = None
    description: Optional[str] = None
    tech_stack: Optional[List[str]] = None


class ProjectResponse(BaseModel):
    id: str
    opportunity_id: str
    user_id: str
    name: str
    tagline: Optional[str]
    description: Optional[str]
    project_structure: Optional[Dict[str, Any]]
    tech_stack: Optional[List[str]]
    status: str
    deploy_url: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}
