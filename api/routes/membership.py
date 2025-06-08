from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database.connection import get_db
from api.database.schemas.membership import (
    MembershipCreate,
    MembershipUpdate,
    MembershipResponse
)
from api.crud import membership as membership_crud

router = APIRouter()


@router.post("/create", response_model=MembershipResponse)
def create_membership(membership: MembershipCreate, db: Session = Depends(get_db)):
    return membership_crud.create_membership(db, membership)

@router.get("/get_all", response_model=List[MembershipResponse])
def list_memberships(db: Session = Depends(get_db)):
    return membership_crud.get_all_memberships(db)

@router.get("/get/{membership_id}", response_model=MembershipResponse)
def get_membership(membership_id: int, db: Session = Depends(get_db)):
    plan = membership_crud.get_membership_by_id(db, membership_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Membership not found")
    return plan

@router.put("/update/{membership_id}", response_model=MembershipResponse)
def update_membership(membership_id: int, updates: MembershipUpdate, db: Session = Depends(get_db)):
    updated = membership_crud.update_membership(db, membership_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Membership not found")
    return updated

@router.delete("/delete/{membership_id}")
def delete_membership(membership_id: int, db: Session = Depends(get_db)):
    deleted = membership_crud.delete_membership(db, membership_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Membership not found")
    return {"detail": "Membership deleted successfully"}


