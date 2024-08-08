from pydantic import BaseModel
from typing import Optional

class LensBase(BaseModel):
    power: str
    coating: str
    branch_id: int
    category: str
    cost: float
    stock: int
    selling_price: float

class LensCreate(LensBase):
    pass

class LensUpdate(BaseModel):
    power: Optional[str] = None
    coating: Optional[str] = None
    branch_id: Optional[int] = None
    category: Optional[str] = None
    cost: Optional[float] = None
    stock: Optional[int] = None
    selling_price: Optional[float] = None

class Lens(LensBase):
    lens_id: int

    class Config:
        orm_mode = True
