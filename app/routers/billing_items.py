# app/routers/billing_items.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.billing_item import BillingItem, BillingItemCreate, BillingItemUpdate
from app.crud.billing_item import get_billing_item, get_billing_items, create_billing_item, update_billing_item, delete_billing_item
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=BillingItem)
def create_new_billing_item(billing_item: BillingItemCreate, db: Session = Depends(get_db)):
    return create_billing_item(db, billing_item)

@router.get("/{billing_item_id}", response_model=BillingItem)
def read_billing_item(billing_item_id: int, db: Session = Depends(get_db)):
    db_billing_item = get_billing_item(db, billing_item_id)
    if db_billing_item is None:
        raise HTTPException(status_code=404, detail="Billing item not found")
    return db_billing_item

@router.get("/", response_model=list[BillingItem])
def read_billing_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    billing_items = get_billing_items(db, skip=skip, limit=limit)
    return billing_items

@router.put("/{billing_item_id}", response_model=BillingItem)
def update_existing_billing_item(billing_item_id: int, billing_item: BillingItemUpdate, db: Session = Depends(get_db)):
    db_billing_item = update_billing_item(db, billing_item_id, billing_item)
    if db_billing_item is None:
        raise HTTPException(status_code=404, detail="Billing item not found")
    return db_billing_item

@router.delete("/{billing_item_id}", response_model=BillingItem)
def delete_existing_billing_item(billing_item_id: int, db: Session = Depends(get_db)):
    db_billing_item = delete_billing_item(db, billing_item_id)
    if db_billing_item is None:
        raise HTTPException(status_code=404, detail="Billing item not found")
    return db_billing_item
