# modules/users/schemas.py

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # instead of orm_mode (for Pydantic v2)

class UserLogin(BaseModel):
    email: EmailStr
    password: str
