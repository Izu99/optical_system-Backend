from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Branch, User

router = APIRouter()

@router.get("/{shop_id}")
def get_dashboard(shop_id: int, db: Session = Depends(get_db)):
    # Fetch all branches for the given shop
    branches = db.query(Branch).filter(Branch.shop_id == shop_id).all()
    
    if not branches:
        raise HTTPException(status_code=404, detail="No branches found for this shop")
    
    # Initialize counts
    optician_count = 0
    fitter_count = 0

    # Aggregate user data
    for branch in branches:
        optician_count += db.query(User).filter(User.branch_id == branch.branch_id, User.role == 'optician').count()
        fitter_count += db.query(User).filter(User.branch_id == branch.branch_id, User.role == 'fitter').count()
    
    return {
        "shop_id": shop_id,
        "branches": [branch.branch_id for branch in branches],
        "opticians": optician_count,
        "fitters": fitter_count
    }
