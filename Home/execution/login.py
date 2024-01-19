from fastapi import APIRouter, Request, Form, Depends, HTTPException, status, Cookie
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from passlib.context import CryptContext
from jose import jwt, ExpiredSignatureError, JWTError
from dotenv import load_dotenv
import secrets



web = APIRouter()
html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

@web.get("/login")
def login(request: Request):
    return html.TemplateResponse("login.html", {"request": request})

@web.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form()):
    # Try to get the user from user_cred
    user = user_cred.find_one({"username": username, "password" : password})
    # pwd_cxt.hash(password)
    if user:
        token = create_access_token(data={"sub": user["username"], "email": user["email"], "role": "user"})
        response_content = {
            "token": token,
            "username": user["username"],
            "email": user["email"],
            "role":"User",
        }
        return JSONResponse(content=response_content, status_code=200)
    
    # If user is not found, try to get the admin from admin_cred
    admin =  admin_cred.find_one({"username": username, "password" : password})
    
    if admin:
        token = create_access_token(data={"sub": admin["username"], "email": admin["email"], "role": "admin"})
        response_content = {
            "token": token,
            "username": admin["username"],
            "email": admin["email"],
            "role": "Admin",
        }
        return JSONResponse(content=response_content, status_code=200)
    
    # If neither user nor admin is found, return invalid credentials
    response_content = {"detail": "Invalid credentials"}
    return JSONResponse(content=response_content, status_code=401)

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def hash_password(pwd: str):   
        return pwd_cxt.hash(pwd)

    def verify_password(pwd: str, hashed_password: str):  
        return pwd_cxt.verify(pwd, hashed_password)

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    
    # Include the role in the token for admin
    if "role" in to_encode:
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    else:
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


from jose import ExpiredSignatureError, JWTError
from fastapi import HTTPException, status

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})
