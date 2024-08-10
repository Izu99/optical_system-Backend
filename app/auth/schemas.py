# app/auth/schemas.py

from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):
    email: str
    password: str

from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str  # Add role to the token schema
    branch_id: int


class TokenData(BaseModel):
    user_id: Optional[str] = None
