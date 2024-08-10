from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.auth.security import decode_token  # Corrected import
from app.auth.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_token(token)
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_user_role(required_role: str, current_user: User = Depends(get_current_user)):
    if current_user.role != required_role:
        raise HTTPException(status_code=403, detail="Forbidden")
    return current_user