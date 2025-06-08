from sqlalchemy.orm import Session
from api.database.models import classes as model
from api.database.schemas import classes as schema

def get_all_classes(db: Session):
    return db.query(model.Class).all()

def get_class_by_id(db: Session, class_id: int):
    return db.query(model.Class).filter(model.Class.id == class_id).first()

def create_classes(db: Session, classes: list[schema.ClassCreate]):
    created = []
    for class_data in classes:
        new_class = model.Class(**class_data.dict())
        db.add(new_class)
        created.append(new_class)
    db.commit()
    for c in created:
        db.refresh(c)
    return created


def update_class(db: Session, class_id: int, class_data: schema.ClassUpdate):
    db_class = db.query(model.Class).filter(model.Class.id == class_id).first()
    if not db_class:
        return None
    for field, value in class_data.dict(exclude_unset=True).items():
        setattr(db_class, field, value)
    db.commit()
    db.refresh(db_class)
    return db_class

def delete_class(db: Session, class_id: int):
    db_class = db.query(model.Class).filter(model.Class.id == class_id).first()
    if db_class:
        db.delete(db_class)
        db.commit()
    return db_class
