from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.branch import create_branch, get_branches, get_branch, update_branch, delete_branch
from app.schemas.branch import Branch, BranchCreate
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Branch)
async def create_branch_endpoint(branch: BranchCreate, db: Session = Depends(get_db)):
    return await create_branch(db, branch)

@router.get("/", response_model=list[Branch])
async def read_branches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_branches(db, skip=skip, limit=limit)

@router.get("/{branch_id}", response_model=Branch)
async def read_branch(branch_id: int, db: Session = Depends(get_db)):
    db_branch = await get_branch(db, branch_id)
    if db_branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return db_branch

@router.put("/{branch_id}", response_model=Branch)
async def update_branch_endpoint(branch_id: int, branch: BranchCreate, db: Session = Depends(get_db)):
    db_branch = await update_branch(db=db, branch_id=branch_id, update_data=branch)
    if db_branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return db_branch


@router.delete("/{branch_id}", response_model=Branch)
async def delete_branch_endpoint(branch_id: int, db: Session = Depends(get_db)):
    db_branch = delete_branch(db=db, branch_id=branch_id)
    if db_branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return db_branch
