# app/crud/lab_equipment.py

from sqlalchemy.orm import Session
from app.models.lab_equipment import LabEquipment
from app.schemas.lab_equipment import LabEquipmentCreate, LabEquipmentUpdate


def create_lab_equipment(db: Session, equipment: LabEquipmentCreate):
    db_equipment = LabEquipment(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


def get_lab_equipment(db: Session, equipment_id: int):
    return db.query(LabEquipment).filter(LabEquipment.equipment_id == equipment_id).first()


def get_lab_equipments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(LabEquipment).offset(skip).limit(limit).all()


def update_lab_equipment(db: Session, equipment_id: int, equipment: LabEquipmentUpdate):
    db_equipment = db.query(LabEquipment).filter(
        LabEquipment.equipment_id == equipment_id).first()
    if db_equipment is None:
        return None
    for key, value in equipment.dict(exclude_unset=True).items():
        setattr(db_equipment, key, value)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


def delete_lab_equipment(db: Session, equipment_id: int):
    db_equipment = db.query(LabEquipment).filter(
        LabEquipment.equipment_id == equipment_id).first()
    if db_equipment:
        db.delete(db_equipment)
        db.commit()
    return db_equipment
