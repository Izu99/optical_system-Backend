# app/crud/billing_item.py
from sqlalchemy.orm import Session
from app.models.billing_item import BillingItem
from app.schemas.billing_item import BillingItemCreate, BillingItemUpdate

def get_billing_item(db: Session, billing_item_id: int):
    return db.query(BillingItem).filter(BillingItem.billing_item_id == billing_item_id).first()

def get_billing_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(BillingItem).offset(skip).limit(limit).all()

def create_billing_item(db: Session, billing_item: BillingItemCreate):
    db_billing_item = BillingItem(**billing_item.dict())
    db.add(db_billing_item)
    db.commit()
    db.refresh(db_billing_item)
    return db_billing_item

def update_billing_item(db: Session, billing_item_id: int, billing_item: BillingItemUpdate):
    db_billing_item = get_billing_item(db, billing_item_id)
    if db_billing_item:
        for key, value in billing_item.dict().items():
            setattr(db_billing_item, key, value)
        db.commit()
        db.refresh(db_billing_item)
    return db_billing_item

def delete_billing_item(db: Session, billing_item_id: int):
    db_billing_item = get_billing_item(db, billing_item_id)
    if db_billing_item:
        db.delete(db_billing_item)
        db.commit()
    return db_billing_item
