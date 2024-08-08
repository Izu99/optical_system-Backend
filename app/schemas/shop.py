# app/schemas/shop.py

from pydantic import BaseModel

class ShopBase(BaseModel):
    name: str
    contact_number: str
    email: str
    headoffice_address: str

class ShopCreate(ShopBase):
    pass

class Shop(ShopBase):
    shop_id: int

    class Config:
        orm_mode: True
