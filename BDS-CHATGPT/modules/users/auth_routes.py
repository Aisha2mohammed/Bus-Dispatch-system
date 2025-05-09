from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from modules.users import models, schemas
from database.connection import get_db
from auth.password_utils import verify_password
from auth.jwt_handler import create_access_token

router = APIRouter()

# @router.post("/login")
# def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.email == user.email).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="Invalid credentials")

#     if not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=401, detail="Incorrect password")

#     token = create_access_token({"sub": db_user.email, "role": db_user.role})
#     return {"access_token": token, "token_type": "bearer"}


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
