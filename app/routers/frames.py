# app/routers/frames.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.frame import Frame, FrameCreate, FrameUpdate
from app.crud.frame import create_frame, get_frame, get_frames, update_frame, delete_frame
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Frame)
def create_new_frame(frame: FrameCreate, db: Session = Depends(get_db)):
    return create_frame(db, frame)

@router.get("/{frame_id}", response_model=Frame)
def read_frame(frame_id: int, db: Session = Depends(get_db)):
    db_frame = get_frame(db, frame_id)
    if db_frame is None:
        raise HTTPException(status_code=404, detail="Frame not found")
    return db_frame

@router.get("/", response_model=list[Frame])
def read_frames(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    frames = get_frames(db, skip=skip, limit=limit)
    return frames

@router.put("/{frame_id}", response_model=Frame)
def update_existing_frame(frame_id: int, frame: FrameUpdate, db: Session = Depends(get_db)):
    db_frame = update_frame(db, frame_id, frame)
    if db_frame is None:
        raise HTTPException(status_code=404, detail="Frame not found")
    return db_frame

@router.delete("/{frame_id}", response_model=Frame)
def delete_existing_frame(frame_id: int, db: Session = Depends(get_db)):
    db_frame = delete_frame(db, frame_id)
    if db_frame is None:
        raise HTTPException(status_code=404, detail="Frame not found")
    return db_frame
