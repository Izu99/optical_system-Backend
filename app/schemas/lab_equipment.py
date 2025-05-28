from pydantic import BaseModel
from typing import Optional

class LabEquipmentBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int

class LabEquipmentCreate(LabEquipmentBase):
    pass

class LabEquipmentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None

class LabEquipment(LabEquipmentBase):
    equipment_id: int

    class Config:
        orm_mode = True
