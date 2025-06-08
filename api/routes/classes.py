from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.crud import classes as crud
from api.database.schemas import classes as schema

router = APIRouter()

@router.get("/get_all", response_model=list[schema.ClassResponse])
def read_classes(db: Session = Depends(get_db)):
    return crud.get_all_classes(db)

@router.get("/get_by_id/{class_id}", response_model=schema.ClassResponse)
def read_class(class_id: int, db: Session = Depends(get_db)):
    class_ = crud.get_class_by_id(db, class_id)
    if not class_:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_

@router.post("/create", response_model=list[schema.ClassResponse])
def create_classes(batch: schema.ClassCreateBatch, db: Session = Depends(get_db)):
    return crud.create_classes(db, batch.classes)


@router.put("/update/{class_id}", response_model=schema.ClassResponse)
def update_class(class_id: int, class_data: schema.ClassUpdate, db: Session = Depends(get_db)):
    updated = crud.update_class(db, class_id, class_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Class not found")
    return updated

@router.delete("/delete/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_class(db, class_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Class not found")
    return {"message": "Class deleted successfully"}
