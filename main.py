# main.py

from fastapi import FastAPI
from modules.users.routes import router as user_router
from modules.users.auth_routes import router as auth_router  # ✅ new line
from database.connection import Base, engine

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include user routes from router
app.include_router(user_router)
