# app/routers/billings.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.billing import Billing, BillingCreate, BillingUpdate
from app.crud.billing import get_billing, get_billings, create_billing, update_billing, delete_billing
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Billing)
def create_new_billing(billing: BillingCreate, db: Session = Depends(get_db)):
    return create_billing(db, billing)

@router.get("/{billing_id}", response_model=Billing)
def read_billing(billing_id: int, db: Session = Depends(get_db)):
    db_billing = get_billing(db, billing_id)
    if db_billing is None:
        raise HTTPException(status_code=404, detail="Billing not found")
    return db_billing

@router.get("/", response_model=list[Billing])
def read_billings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    billings = get_billings(db, skip=skip, limit=limit)
    return billings

@router.put("/{billing_id}", response_model=Billing)
def update_existing_billing(billing_id: int, billing: BillingUpdate, db: Session = Depends(get_db)):
    db_billing = update_billing(db, billing_id, billing)
    if db_billing is None:
        raise HTTPException(status_code=404, detail="Billing not found")
    return db_billing

@router.delete("/{billing_id}", response_model=Billing)
def delete_existing_billing(billing_id: int, db: Session = Depends(get_db)):
    db_billing = delete_billing(db, billing_id)
    if db_billing is None:
        raise HTTPException(status_code=404, detail="Billing not found")
    return db_billing
