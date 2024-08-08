from sqlalchemy.orm import Session
from app.models.lens import Lens
from app.models.branch import Branch
from app.schemas.lens import LensCreate, LensUpdate

def create_lens(db: Session, lens: LensCreate):
    branch_exists = db.query(Branch).filter(
        Branch.branch_id == lens.branch_id).first()
    if not branch_exists:
        raise ValueError("The specified branch does not exist.")
    db_lens = Lens(**lens.dict())
    db.add(db_lens)
    db.commit()
    db.refresh(db_lens)
    return db_lens

def get_lens(db: Session, lens_id: int):
    return db.query(Lens).filter(Lens.lens_id == lens_id).first()

def get_lenses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Lens).offset(skip).limit(limit).all()

def update_lens(db: Session, lens_id: int, lens_update: LensUpdate):
    db_lens = db.query(Lens).filter(Lens.lens_id == lens_id).first()
    if db_lens:
        for key, value in lens_update.dict(exclude_unset=True).items():
            setattr(db_lens, key, value)
        db.commit()
        db.refresh(db_lens)
    return db_lens

def delete_lens(db: Session, lens_id: int):
    db_lens = db.query(Lens).filter(Lens.lens_id == lens_id).first()
    if db_lens:
        db.delete(db_lens)
        db.commit()
    return db_lens
