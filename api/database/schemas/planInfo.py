from pydantic import BaseModel
from typing import Optional

class PlanInfoBase(BaseModel):
    membership_id: int
    line_1: Optional[str] = None
    line_2: Optional[str] = None
    line_3: Optional[str] = None
    line_4: Optional[str] = None
    line_5: Optional[str] = None
    line_6: Optional[str] = None
    line_7: Optional[str] = None

class PlanInfoCreate(PlanInfoBase):
    pass

class PlanInfoUpdate(PlanInfoBase):
    pass

class PlanInfoResponse(PlanInfoBase):
    id: int

    class Config:
        from_attributes = True
