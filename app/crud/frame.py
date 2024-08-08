# app/crud/frame.py
from sqlalchemy.orm import Session
from app.models.frame import Frame as FrameModel
from app.models.branch import Branch
from app.schemas.frame import FrameCreate, FrameUpdate


def create_frame(db: Session, frame: FrameCreate):
    branch_exists = db.query(Branch).filter(
        Branch.branch_id == frame.branch_id).first()
    if not branch_exists:
        raise ValueError("The specified branch does not exist.")
    db_frame = FrameModel(**frame.dict())
    db.add(db_frame)
    db.commit()
    db.refresh(db_frame)
    return db_frame


def get_frame(db: Session, frame_id: int):
    return db.query(FrameModel).filter(FrameModel.frame_id == frame_id).first()


def get_frames(db: Session, skip: int = 0, limit: int = 10):
    return db.query(FrameModel).offset(skip).limit(limit).all()


def update_frame(db: Session, frame_id: int, frame_update: FrameUpdate):
    db_frame = db.query(FrameModel).filter(
        FrameModel.frame_id == frame_id).first()
    if db_frame:
        for key, value in frame_update.dict(exclude_unset=True).items():
            setattr(db_frame, key, value)
        db.commit()
        db.refresh(db_frame)
    return db_frame


def delete_frame(db: Session, frame_id: int):
    db_frame = db.query(FrameModel).filter(
        FrameModel.frame_id == frame_id).first()
    if db_frame:
        db.delete(db_frame)
        db.commit()
    return db_frame
