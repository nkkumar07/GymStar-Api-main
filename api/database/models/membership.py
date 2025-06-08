from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from api.database.connection import Base

class MembershipPlan(Base):
    __tablename__ = "membership_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, default=0.0)  # New field
    final_price = Column(Float, nullable=False)  # New field
    duration = Column(String(50), nullable=False)  # Monthly, Half Yearly, Yearly
    plan_info = Column(Text, nullable=True)  # New field
    status = Column(String(50), default="active")
    created = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # New field
