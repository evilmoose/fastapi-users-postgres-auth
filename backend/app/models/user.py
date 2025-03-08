"""
Database models for users with fastapi-users integration
"""
from sqlalchemy import Column, Integer, String, Boolean, Table
from fastapi_users.db import SQLAlchemyBaseUserTable

from app.core.db import Base

class User(SQLAlchemyBaseUserTable[int], Base):
    """
    User model for fastapi-users integration
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    first_name = Column(String(length=50), nullable=True)
    last_name = Column(String(length=50), nullable=True)
    
