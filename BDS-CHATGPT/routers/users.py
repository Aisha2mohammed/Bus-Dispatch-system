# from fastapi import FastAPI
# from routers import users  # ← import your users module

# from fastapi import APIRouter
# from pydantic import BaseModel
# from typing import List

# router = APIRouter()

# # In-memory users list
# users = []

# class User(BaseModel):
#     username: str
#     email: str
#     role: str  # admin, driver, owner, dispatcher, chaser

# @router.post("/users")
# def create_user(user: User):
#     users.append(user)
#     return {"message": "User created", "user": user}

# @router.get("/users", response_model=List[User])
# def list_users():
#     return users

# @router.get("/users/{username}")
# def get_user(username: str):
#     for user in users:
#         if user.username == username:
#             return user
#     return {"error": "User not found"}

# @router.put("/users/{username}")
# def update_user(username: str, updated_user: User):
#     for i, user in enumerate(users):
#         if user.username == username:
#             users[i] = updated_user
#             return {"message": "User updated", "user": updated_user}
#     return {"error": "User not found"}

# @router.delete("/users/{username}")
# def delete_user(username: str):
#     for i, user in enumerate(users):
#         if user.username == username:
#             deleted = users.pop(i)
#             return {"message": "User deleted", "user": deleted}
#     return {"error": "User not found"}





from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to view users")
    return db.query(models.User).all()

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to view user details")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to create users")
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/{user_id}")
def update_user(user_id: int, updated_data: schemas.UserUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to update users")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in updated_data.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to delete users")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}