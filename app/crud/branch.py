from sqlalchemy.orm import Session
from app.models.branch import Branch as BranchModel
from app.schemas.branch import BranchCreate

async def create_branch(db: Session, branch: BranchCreate):
    db_branch = BranchModel(
        contact_number=branch.contact_number,
        branch_code=branch.branch_code,
        branch_name=branch.branch_name,
        shop_id=branch.shop_id
    )
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

async def get_branches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(BranchModel).offset(skip).limit(limit).all()

async def get_branch(db: Session, branch_id: int):
    return db.query(BranchModel).filter(BranchModel.branch_id == branch_id).first()

async def update_branch(db: Session, branch_id: int, update_data: BranchCreate):
    db_branch = db.query(BranchModel).filter(BranchModel.branch_id == branch_id).first()
    if db_branch:
        db_branch.contact_number = update_data.contact_number
        db_branch.branch_code = update_data.branch_code
        db_branch.branch_name = update_data.branch_name
        db_branch.shop_id = update_data.shop_id
        db.commit()
        db.refresh(db_branch)
    return db_branch

def delete_branch(db: Session, branch_id: int):
    db_branch = db.query(BranchModel).filter(BranchModel.branch_id == branch_id).first()
    if db_branch:
        db.delete(db_branch)
        db.commit()
        return db_branch
    return None
