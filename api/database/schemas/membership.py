from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MembershipCreate(BaseModel):
    name: str
    price: float
    discount: Optional[float] = 0.0
    final_price: float
    duration: str  # Monthly, Half Yearly, Yearly
    plan_info: Optional[str] = None
    status: Optional[str] = "active"

class MembershipUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]
    discount: Optional[float]
    final_price: Optional[float]
    duration: Optional[str]
    plan_info: Optional[str]
    status: Optional[str]

class MembershipResponse(BaseModel):
    id: int
    name: str
    price: float
    discount: float
    final_price: float
    duration: str
    plan_info: Optional[str]
    status: str
    created: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
