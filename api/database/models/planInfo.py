from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.database.connection import Base

class PlanInfo(Base):
    __tablename__ = "plan_info"

    id = Column(Integer, primary_key=True, index=True)
    membership_id = Column(Integer, ForeignKey("membership_plans.id"), nullable=False)

    line_1 = Column(String(255))
    line_2 = Column(String(255))
    line_3 = Column(String(255))
    line_4 = Column(String(255))
    line_5 = Column(String(255))
    line_6 = Column(String(255))
    line_7 = Column(String(255))

 