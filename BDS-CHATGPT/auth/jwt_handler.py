# from datetime import datetime, timedelta
# from jose import JWTError, jwt

# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from database.connection import get_db
# from modules.users.models import User

# # 🔐 WARNING: Change this in production!
# SECRET_KEY = "supersecretkey"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def decode_access_token(token: str):
#     try:
#         return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     except JWTError:
#         return None

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     payload = decode_access_token(token)
#     if not payload:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")

#     user = db.query(User).filter(User.email == payload["sub"]).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     return user






from datetime import datetime, timedelta
from jose import JWTError, jwt

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database.connection import get_db
from modules.users.models import User


# Secret key — change this in production!
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(User).filter(User.email == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user