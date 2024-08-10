# app/crud/user.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User, UserRole
from app.models.branch import Branch
from app.schemas.user import UserCreate, UserUpdate
from app.auth.security import hash_password  # Ensure this import is correct

def create_user(db: Session, user: UserCreate):
    # Check if the branch exists
    branch_exists = db.query(Branch).filter(Branch.branch_id == user.branch_id).first()
    if not branch_exists:
        raise ValueError("The specified branch does not exist.")
    
    # Check if a user with the same role and branch_id already exists for owner or manager roles
    if user.role in {UserRole.owner, UserRole.manager}:
        existing_user = db.query(User).filter(
            User.branch_id == user.branch_id,
            User.role == user.role
        ).first()
        
        if existing_user:
            raise ValueError(f"A user with the role {user.role} already exists in branch {user.branch_id}.")
    
    # Hash the password before saving it
    hashed_password = hash_password(user.password)
    
    # Create and add the new user
    db_user = User(
        email=user.email,
        password=hashed_password,  # Save hashed password
        role=user.role,
        branch_id=user.branch_id
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        # Handle specific error cases
        if 'users.email' in str(e.orig):
            raise ValueError("A user with this email already exists.")
        else:
            raise ValueError("An unexpected error occurred.")

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            if key == "password" and value:  # Hash password if it's being updated
                value = hash_password(value)
            setattr(db_user, key, value)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None
