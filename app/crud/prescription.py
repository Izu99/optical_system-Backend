# app/crud/prescription.py

from sqlalchemy.orm import Session
from app.models.prescription import Prescription
from app.schemas.prescription import PrescriptionCreate, PrescriptionUpdate

def create_prescription(db: Session, prescription: PrescriptionCreate):
    db_prescription = Prescription(**prescription.dict())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

def get_prescription(db: Session, prescription_id: int):
    return db.query(Prescription).filter(Prescription.prescription_id == prescription_id).first()

def get_prescriptions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Prescription).offset(skip).limit(limit).all()

def update_prescription(db: Session, prescription_id: int, prescription: PrescriptionUpdate):
    db_prescription = db.query(Prescription).filter(Prescription.prescription_id == prescription_id).first()
    if db_prescription:
        for key, value in prescription.dict(exclude_unset=True).items():
            setattr(db_prescription, key, value)
        db.commit()
        db.refresh(db_prescription)
    return db_prescription

def delete_prescription(db: Session, prescription_id: int):
    db_prescription = db.query(Prescription).filter(Prescription.prescription_id == prescription_id).first()
    if db_prescription:
        db.delete(db_prescription)
        db.commit()
    return db_prescription
