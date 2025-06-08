from sqlalchemy.orm import Session
from api.database.models.membership import MembershipPlan
from api.database.schemas.membership import MembershipCreate, MembershipUpdate

def create_membership(db: Session, membership: MembershipCreate):
    db_plan = MembershipPlan(
        **membership.dict()
    )
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


def get_all_memberships(db: Session):
    return db.query(MembershipPlan).all()

def get_membership_by_id(db: Session, membership_id: int):
    return db.query(MembershipPlan).filter(MembershipPlan.id == membership_id).first()

def update_membership(db: Session, membership_id: int, updates: MembershipUpdate):
    db_plan = get_membership_by_id(db, membership_id)
    if not db_plan:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_plan, key, value)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def delete_membership(db: Session, membership_id: int):
    db_plan = get_membership_by_id(db, membership_id)
    if not db_plan:
        return False
    db.delete(db_plan)
    db.commit()
    return True


