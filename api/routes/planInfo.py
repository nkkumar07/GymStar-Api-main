from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.planInfo import PlanInfoCreate, PlanInfoResponse, PlanInfoUpdate
from api.crud import planInfo as crud

router = APIRouter()

@router.get("/get_all", response_model=list[PlanInfoResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_plan_infos(db)

@router.get("/get_by_membership_id/{membership_id}", response_model=list[PlanInfoResponse])
def get_by_membership_id(membership_id: int, db: Session = Depends(get_db)):
    plan_infos = crud.get_plan_info_by_membership_id(db, membership_id)
    if not plan_infos:
        raise HTTPException(status_code=404, detail="No PlanInfo found for this membership_id")
    return plan_infos


@router.get("/get_by_id/{plan_id}", response_model=PlanInfoResponse)
def read_by_id(plan_id: int, db: Session = Depends(get_db)):
    plan = crud.get_plan_info_by_id(db, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="PlanInfo not found")
    return plan

@router.post("/post", response_model=PlanInfoResponse)
def create(plan_data: PlanInfoCreate, db: Session = Depends(get_db)):
    return crud.create_plan_info(db, plan_data)

@router.put("/update/{plan_id}", response_model=PlanInfoResponse)
def update(plan_id: int, plan_data: PlanInfoUpdate, db: Session = Depends(get_db)):
    plan = crud.update_plan_info(db, plan_id, plan_data)
    if not plan:
        raise HTTPException(status_code=404, detail="PlanInfo not found")
    return plan

    
@router.put("/update_by_membership_id/{membership_id}", response_model=PlanInfoResponse)
def update_by_membership_id(membership_id: int, plan_data: PlanInfoUpdate, db: Session = Depends(get_db)):
    plan = crud.update_plan_info_by_membership_id(db, membership_id, plan_data)
    if not plan:
        raise HTTPException(status_code=404, detail="PlanInfo with this membership_id not found")
    return plan

@router.delete("/delete/{plan_id}", response_model=PlanInfoResponse)
def delete(plan_id: int, db: Session = Depends(get_db)):
    plan = crud.delete_plan_info(db, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="PlanInfo not found")
    return plan
