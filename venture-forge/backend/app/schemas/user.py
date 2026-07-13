from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from ..models.user import PlanType


class UserCreate(BaseModel):
    clerk_id: str
    email: EmailStr
    name: Optional[str] = None
    avatar_url: Optional[str] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    plan: Optional[PlanType] = None


class UserResponse(BaseModel):
    id: str
    email: str
    name: Optional[str]
    avatar_url: Optional[str]
    plan: PlanType
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}
