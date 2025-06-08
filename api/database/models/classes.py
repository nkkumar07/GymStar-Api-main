from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from api.database.connection import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"), nullable=False)
    day = Column(String(255), nullable=False)
    class_name = Column(String(255), nullable=False)
    timeing = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
