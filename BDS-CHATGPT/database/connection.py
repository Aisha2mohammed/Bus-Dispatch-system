
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # PostgreSQL DB URL
# SQLALCHEMY_DATABASE_URL = "postgresql://dispatch_user:strongpassword@localhost/bus_dispatch_db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


# # ✅ This function MUST exist
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()






from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB URL — update as needed
SQLALCHEMY_DATABASE_URL = "postgresql://dispatch_user:strongpassword@localhost/bus_dispatch_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
