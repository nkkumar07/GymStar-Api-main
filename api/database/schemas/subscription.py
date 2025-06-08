from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SubscriptionCreate(BaseModel):
    user_id: int
    membership_id: int
    start_date: datetime
    expiry_date: datetime
    subtotal: float
    discount: Optional[float] = 0.0
    total: float
    promocode: Optional[str] = None
    payment_status: Optional[str] = "pending"

class SubscriptionUpdate(BaseModel):
    start_date: Optional[datetime]
    expiry_date: Optional[datetime]
    subtotal: Optional[float]
    discount: Optional[float]
    total: Optional[float]
    promocode: Optional[str]
    payment_status: Optional[str]

class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    membership_id: int
    start_date: datetime
    expiry_date: datetime
    subtotal: float
    discount: float
    total: float
    promocode: Optional[str]
    payment_status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
