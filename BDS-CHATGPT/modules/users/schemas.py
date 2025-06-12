
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
