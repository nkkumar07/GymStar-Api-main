from sqlalchemy.orm import Session
from api.database.models.subscription import Subscription
from api.database.schemas.subscription import SubscriptionCreate, SubscriptionUpdate

def create_subscription(db: Session, sub_data: SubscriptionCreate):
    new_sub = Subscription(**sub_data.dict())
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return new_sub

def get_all_subscriptions(db: Session):
    return db.query(Subscription).all()

def get_subscription_by_id(db: Session, sub_id: int):
    return db.query(Subscription).filter(Subscription.id == sub_id).first()

def update_subscription(db: Session, sub_id: int, updates: SubscriptionUpdate):
    subscription = get_subscription_by_id(db, sub_id)
    if not subscription:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(subscription, key, value)
    db.commit()
    db.refresh(subscription)
    return subscription

def delete_subscription(db: Session, sub_id: int):
    subscription = get_subscription_by_id(db, sub_id)
    if not subscription:
        return False
    db.delete(subscription)
    db.commit()
    return True


def get_subscriptions_by_user_id(db: Session, user_id: int):
    return db.query(Subscription).filter(Subscription.user_id == user_id).all()
