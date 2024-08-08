# app/routers/prescriptions.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.prescription import Prescription, PrescriptionCreate, PrescriptionUpdate
from app.crud.prescription import create_prescription, get_prescription, get_prescriptions, update_prescription, delete_prescription
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Prescription)
def create_new_prescription(prescription: PrescriptionCreate, db: Session = Depends(get_db)):
    return create_prescription(db, prescription)

@router.get("/{prescription_id}", response_model=Prescription)
def read_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = get_prescription(db, prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription

@router.get("/", response_model=list[Prescription])
def read_prescriptions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_prescriptions(db, skip=skip, limit=limit)

@router.put("/{prescription_id}", response_model=Prescription)
def update_existing_prescription(prescription_id: int, prescription: PrescriptionUpdate, db: Session = Depends(get_db)):
    db_prescription = update_prescription(db, prescription_id, prescription)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription

@router.delete("/{prescription_id}", response_model=Prescription)
def delete_existing_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = delete_prescription(db, prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription
