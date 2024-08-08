# app/schemas/frame.py
from pydantic import BaseModel
from typing import Optional

class FrameBase(BaseModel):
    brand: str
    size: str
    whole_sale_price: float
    color: str
    model: str
    selling_price: float
    stock: int
    branch_id: int

class FrameCreate(FrameBase):
    pass

class FrameUpdate(BaseModel):
    brand: Optional[str] = None
    size: Optional[str] = None
    whole_sale_price: Optional[float] = None
    color: Optional[str] = None
    model: Optional[str] = None
    selling_price: Optional[float] = None
    stock: Optional[int] = None
    branch_id: Optional[int] = None

class Frame(FrameBase):
    frame_id: int

    class Config:
        orm_mode = True
