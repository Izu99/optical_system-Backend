from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.security import create_access_token, verify_password
from app.models.user import User
from app.auth.schemas import Token, UserLogin
from app.auth.dependencies import get_current_user_role

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(user_login: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_login.email).first()
    if user and verify_password(user_login.password, user.password):
        # Prepare the data to include in the token
        token_data = {"user_id": user.user_id, "role": user.role}
        # Create the token with the data
        token = create_access_token(data=token_data)
        
        return {
            "access_token": token,
            "token_type": "bearer",
            "role": user.role  # Include the role in the response
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
@router.get("/owner", response_model=str)
def owner_page(current_user: User = Depends(lambda: get_current_user_role("owner"))):
    return "Welcome to the owner page"

@router.get("/manager", response_model=str)
def manager_page(current_user: User = Depends(lambda: get_current_user_role("manager"))):
    return "Welcome to the manager page"

@router.get("/optician", response_model=str)
def optician_page(current_user: User = Depends(lambda: get_current_user_role("optician"))):
    return "Welcome to the optician page"

@router.get("/fitter", response_model=str)
def fitter_page(current_user: User = Depends(lambda: get_current_user_role("fitter"))):
    return "Welcome to the fitter page"
