

from fastapi import FastAPI
from modules.users.routes import router as user_router
from modules.users.auth_routes import router as auth_router
from database.connection import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from modules.users.models import User
from utils.hashing import Hash  # Make sure this is your actual hasher

def create_admin_user():
    db: Session = SessionLocal()
    existing_admin = db.query(User).filter(User.email == "admin@example.com").first()
    if not existing_admin:
        admin_user = User(
            username="admin",
            email="admin@example.com",
            password=Hash.bcrypt("admin123"),
            role="admin"
        )
        db.add(admin_user)
        db.commit()
        print("✅ Admin user created.")
    else:
        print("ℹ️ Admin already exists.")
    db.close()

app = FastAPI()

# Auto-create database tables
Base.metadata.create_all(bind=engine)

# Call the admin seeder here (optional to remove later)
create_admin_user()

# Include routers
app.include_router(user_router, prefix="/api", tags=["Users"])
app.include_router(auth_router, prefix="/api", tags=["Auth"])
