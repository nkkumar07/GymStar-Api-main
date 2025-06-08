from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.database.connection import get_db
from api.database.schemas.subscription import (
    SubscriptionCreate,
    SubscriptionUpdate,
    SubscriptionResponse,
)
from api.crud import subscription as crud

router = APIRouter()

@router.post("/", response_model=SubscriptionResponse)
def create(sub: SubscriptionCreate, db: Session = Depends(get_db)):
    return crud.create_subscription(db, sub)

@router.get("/", response_model=List[SubscriptionResponse])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_subscriptions(db)

@router.get("/{sub_id}", response_model=SubscriptionResponse)
def get_by_id(sub_id: int, db: Session = Depends(get_db)):
    subscription = crud.get_subscription_by_id(db, sub_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@router.put("/{sub_id}", response_model=SubscriptionResponse)
def update(sub_id: int, updates: SubscriptionUpdate, db: Session = Depends(get_db)):
    updated = crud.update_subscription(db, sub_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return updated

@router.delete("/{sub_id}")
def delete(sub_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_subscription(db, sub_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"detail": "Subscription deleted successfully"}




@router.get("/by_user/{user_id}", response_model=List[SubscriptionResponse])
def get_by_user_id(user_id: int, db: Session = Depends(get_db)):
    subscriptions = crud.get_subscriptions_by_user_id(db, user_id)
    if not subscriptions:
        raise HTTPException(status_code=404, detail="No subscriptions found for this user")
    return subscriptions
