from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request, Form, HTTPException, status, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import user_cred, admin_cred
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, ExpiredSignatureError, JWTError

web = APIRouter()
html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

SECRET_KEY = "yourkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def hash_password(pwd: str):
        return pwd_cxt.hash(pwd)

    def verify_password(pwd: str, hashed_password: str):  
        return pwd_cxt.verify(pwd, hashed_password)


def create_jwt_token(user,role):
    credentials = {"sub": user["username"], "email": user["email"], "role": role}
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = credentials.copy()
    expire = datetime.utcnow() + expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "yourkey", algorithm="HS256")
    return encoded_jwt

def decode_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    # Check token expiration
        if payload["exp"] <= datetime.utcnow().timestamp():
            raise ExpiredSignatureError("Token has expired")
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired",
                            headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token",
                            headers={"WWW-Authenticate": "Bearer"})
    
@web.get("/login")
def login(request: Request):
    return html.TemplateResponse("login.html", {"request": request})


@web.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form()):
    
    user = user_cred.find_one({"username": username})
    try:
        if user and Hash.verify_password(password, user["password"]) :
            token = create_jwt_token(user, role="user")
            response_content = {
                "token": token,
                "username": user["username"],
                "email": user["email"],
                "role":"User",
            }
            return JSONResponse(content=response_content, status_code=200)
    
    
        admin = admin_cred.find_one({"username": username})
   
        if admin and Hash.verify_password(password, admin["password"]):
            token = create_jwt_token(admin, role="admin")
            response_content = {
                "token": token,
                "username": admin["username"],
                "email": admin["email"],
                "role": "Admin",
            }
            return JSONResponse(content=response_content, status_code=200) 
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)