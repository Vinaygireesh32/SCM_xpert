from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
import jwt
import datetime

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

# Secret key for JWT (change it to a strong and secure key in production)
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Function to generate a JWT token
def create_jwt_token(username: str) -> str:
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    payload = {"sub": username, "exp": expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(token)
    return token

@web.get("/login")
def login(request : Request):
    return html.TemplateResponse("login.html", {"request": request})

@web.post("/login")
def login(request : Request, username : str = Form(), password : str = Form()):
    var = user_cred.find_one({ "$and" : [ {"username":username},{"password":password} ] })
    adm = admin_cred.find_one({ "$and" : [ {"username":username},{"password":password} ] })
    
    if var:
        token = create_jwt_token(username)
        return html.TemplateResponse("dashboard.html", {"request": request, "token":token})
    elif adm:
        token = create_jwt_token(username)
        return html.TemplateResponse("admin.html", {"request": request, "token":token})
    return html.TemplateResponse("login.html", {"request": request})
    

# from fastapi import APIRouter, Request, Depends, Form, HTTPException, status
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from fastapi.security import OAuth2PasswordBearer
# from execute.execute import *
# import jwt
# import datetime

# web = APIRouter()

# html = Jinja2Templates(directory="html")
# web.mount("/static", StaticFiles(directory="static"), name="static")

# # Secret key for JWT (change it to a strong and secure key in production)
# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"

# # Function to generate a JWT token
# def create_jwt_token(username: str) -> str:
#     expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
#     payload = {"sub": username, "exp": expiration_time}
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#     return token

# # OAuth2 scheme for token authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Dependency function to get current user from JWT token
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except jwt.ExpiredSignatureError:
#         raise credentials_exception
#     except jwt.JWTError:
#         raise credentials_exception
#     return username

# @web.get("/login")
# def login(request: Request):
#     return html.TemplateResponse("login.html", {"request": request})

# @web.post("/login")
# def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
#     var = user_cred.find_one({"$and": [{"username": username}, {"password": password}]})
#     adm = admin_cred.find_one({"$and": [{"username": username}, {"password": password}]})

#     if var:
#         token = create_jwt_token(username)
#         return html.TemplateResponse("user.html", {"request": request, "token": token})
#     elif adm:
#         token = create_jwt_token(username)
#         return html.TemplateResponse("admin.html", {"request": request, "token": token})
#     return html.TemplateResponse("login.html", {"request": request})

# @web.get("/protected")
# async def protected_route(request: Request, current_user: str = Depends(get_current_user)):
#     return html.TemplateResponse("protected.html", {"request": request, "current_user": current_user})

   
