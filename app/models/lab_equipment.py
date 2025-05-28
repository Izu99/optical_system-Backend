from sqlalchemy import Column, Integer, String
from app.database import Base  # assuming you have a Base in database.py

class LabEquipment(Base):
    __tablename__ = "lab_equipments"

    equipment_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False, default=0)
