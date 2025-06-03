from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from modules.users import models, schemas
from database.connection import get_db
from auth.password_utils import verify_password
from auth.jwt_handler import create_access_token

router = APIRouter()

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass  # Add optional password update here if needed

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2

class UserLogin(BaseModel):
    email: EmailStr
    password: str
