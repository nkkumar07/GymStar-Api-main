from sqlalchemy.orm import Session
from api.database.models.planInfo import PlanInfo
from api.database.schemas.planInfo import PlanInfoCreate, PlanInfoUpdate
from fastapi import HTTPException

def get_all_plan_infos(db: Session):
    return db.query(PlanInfo).all()

def get_plan_info_by_id(db: Session, plan_id: int):
    return db.query(PlanInfo).filter(PlanInfo.id == plan_id).first()

def get_plan_info_by_membership_id(db: Session, membership_id: int):
    return db.query(PlanInfo).filter(PlanInfo.membership_id == membership_id).all()


def create_plan_info(db: Session, plan_data: PlanInfoCreate):
    # Check for duplicate membership_id
    existing_plan = db.query(PlanInfo).filter(PlanInfo.membership_id == plan_data.membership_id).first()
    if existing_plan:
        raise HTTPException(status_code=400, detail="PlanInfo with this membership_id already exists")

    db_plan = PlanInfo(**plan_data.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def update_plan_info(db: Session, plan_id: int, plan_data: PlanInfoUpdate):
    db_plan = db.query(PlanInfo).filter(PlanInfo.id == plan_id).first()
    if db_plan:
        for key, value in plan_data.dict(exclude_unset=True).items():
            setattr(db_plan, key, value)
        db.commit()
        db.refresh(db_plan)
    return db_plan

def update_plan_info_by_membership_id(db: Session, membership_id: int, plan_data: PlanInfoUpdate):
    db_plan = db.query(PlanInfo).filter(PlanInfo.membership_id == membership_id).first()
    if db_plan:
        for key, value in plan_data.dict(exclude_unset=True).items():
            setattr(db_plan, key, value)
        db.commit()
        db.refresh(db_plan)
    return db_plan

def delete_plan_info(db: Session, plan_id: int):
    db_plan = db.query(PlanInfo).filter(PlanInfo.id == plan_id).first()
    if db_plan:
        db.delete(db_plan)
        db.commit()
    return db_plan
