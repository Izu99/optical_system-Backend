# app/models/__init__.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models.shop import Shop
from app.models.branch import Branch
from app.models.user import User