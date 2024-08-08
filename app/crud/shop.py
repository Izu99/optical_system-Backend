# app/crud/shop.py

from sqlalchemy.orm import Session
from app.models.shop import Shop as ShopModel
from app.schemas.shop import ShopCreate

async def create_shop(db: Session, shop: ShopCreate):
    db_shop = ShopModel(
        name=shop.name,
        contact_number=shop.contact_number,
        email=shop.email,
        headoffice_address=shop.headoffice_address
    )
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop

async def get_shops(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ShopModel).offset(skip).limit(limit).all()

async def get_shop(db: Session, shop_id: int):
    return db.query(ShopModel).filter(ShopModel.shop_id == shop_id).first()

async def update_shop(db: Session, shop_id: int, update_data: ShopCreate):
    db_shop = db.query(ShopModel).filter(ShopModel.shop_id == shop_id).first()
    if db_shop:
        db_shop.name = update_data.name
        db_shop.contact_number = update_data.contact_number
        db_shop.email = update_data.email
        db_shop.headoffice_address = update_data.headoffice_address
        db.commit()
        db.refresh(db_shop)
    return db_shop

def delete_shop(db: Session, shop_id: int):
    db_shop = db.query(ShopModel).filter(ShopModel.shop_id == shop_id).first()
    if db_shop:
        db.delete(db_shop)
        db.commit()
        return db_shop
    return None
