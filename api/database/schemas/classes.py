from pydantic import BaseModel
from typing import Optional
from typing import List

class ClassBase(BaseModel):
    trainer_id: int
    day: str
    class_name: str
    timeing: str

class ClassCreate(ClassBase):
    pass

class ClassCreateBatch(BaseModel):
    classes: List[ClassCreate]

class ClassUpdate(BaseModel):
    trainer_id: Optional[int]
    day: Optional[str]
    class_name: Optional[str]
    timeing: Optional[str]

class ClassResponse(ClassBase):
    id: int
    class Config:
        from_attributes = True
