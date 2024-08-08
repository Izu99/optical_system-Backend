# app/routers/shops.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.shop import Shop, ShopCreate
from app.crud.shop import create_shop, get_shops, get_shop, update_shop, delete_shop
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Shop)
async def create_shop_endpoint(shop: ShopCreate, db: Session = Depends(get_db)):
    return await create_shop(db=db, shop=shop)

@router.get("/", response_model=list[Shop])
async def get_shops_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_shops(db=db, skip=skip, limit=limit)

@router.get("/{shop_id}", response_model=Shop)
async def get_shop_endpoint(shop_id: int, db: Session = Depends(get_db)):
    db_shop = await get_shop(db=db, shop_id=shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop

@router.put("/{shop_id}", response_model=Shop)
async def update_shop_endpoint(shop_id: int, shop: ShopCreate, db: Session = Depends(get_db)):
    db_shop = await update_shop(db=db, shop_id=shop_id, update_data=shop)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop


@router.delete("/{shop_id}", response_model=Shop)
async def delete_shop_endpoint(shop_id: int, db: Session = Depends(get_db)):
    db_shop = delete_shop(db=db, shop_id=shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop