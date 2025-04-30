from fastapi import FastAPI
from routers import users  # ← import your users module

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# In-memory users list
users = []

class User(BaseModel):
    username: str
    email: str
    role: str  # admin, driver, owner, dispatcher, chaser

@router.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}

@router.get("/users", response_model=List[User])
def list_users():
    return users

@router.get("/users/{username}")
def get_user(username: str):
    for user in users:
        if user.username == username:
            return user
    return {"error": "User not found"}

@router.put("/users/{username}")
def update_user(username: str, updated_user: User):
    for i, user in enumerate(users):
        if user.username == username:
            users[i] = updated_user
            return {"message": "User updated", "user": updated_user}
    return {"error": "User not found"}

@router.delete("/users/{username}")
def delete_user(username: str):
    for i, user in enumerate(users):
        if user.username == username:
            deleted = users.pop(i)
            return {"message": "User deleted", "user": deleted}
    return {"error": "User not found"}
