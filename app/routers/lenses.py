from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.lens import Lens, LensCreate, LensUpdate
from app.crud.lens import create_lens, get_lens, get_lenses, update_lens, delete_lens
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Lens)
def create_new_lens(lens: LensCreate, db: Session = Depends(get_db)):
    return create_lens(db, lens)

@router.get("/{lens_id}", response_model=Lens)
def read_lens(lens_id: int, db: Session = Depends(get_db)):
    db_lens = get_lens(db, lens_id)
    if db_lens is None:
        raise HTTPException(status_code=404, detail="Lens not found")
    return db_lens

@router.get("/", response_model=list[Lens])
def read_lenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    lenses = get_lenses(db, skip=skip, limit=limit)
    return lenses

@router.put("/{lens_id}", response_model=Lens)
def update_existing_lens(lens_id: int, lens: LensUpdate, db: Session = Depends(get_db)):
    db_lens = update_lens(db, lens_id, lens)
    if db_lens is None:
        raise HTTPException(status_code=404, detail="Lens not found")
    return db_lens

@router.delete("/{lens_id}", response_model=Lens)
def delete_existing_lens(lens_id: int, db: Session = Depends(get_db)):
    db_lens = delete_lens(db, lens_id)
    if db_lens is None:
        raise HTTPException(status_code=404, detail="Lens not found")
    return db_lens
