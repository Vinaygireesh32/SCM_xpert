import re
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from execution.login import *
from passlib.context import CryptContext

web = APIRouter()

html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

password_pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

@web.get("/signup")
def Signup(signdata: Request):
    return html.TemplateResponse("signup.html", {"request": signdata, "error_message": None})

@web.post("/signup")
def Signup(request: Request, Username: str = Form(), Email: str = Form(), Create_Password: str = Form(), Confirm_Password: str = Form()):
    # Check if user already exists
    if user_cred.find_one({'username': Username}):
        error_message = "User already registered **"
        return html.TemplateResponse("signup.html", {"request": request, "error_message": error_message})
    if user_cred.find_one({'email': Email}):
        error_message = "Email already registered **"
        return html.TemplateResponse("signup.html", {"request": request, "error_message": error_message})

    # Validate password
    if not password_pattern.match(Create_Password):
        error_message = "Password doesn't match the expectations"
        return html.TemplateResponse("signup.html", {"request": request, "error_message": error_message})

    # Validate email
    if not email_pattern.match(Email):
        error_message = "Invalid email format ** "
        return html.TemplateResponse("signup.html", {"request": request, "error_message": error_message})

    # Check if passwords match
    if Create_Password != Confirm_Password:
        error_message = "Passwords doesn't match"
        return html.TemplateResponse("signup.html", {"request": request, "error_message": error_message})

    # Hash the password before storing it in the database
    
    pw = pwd_cxt.hash(Create_Password)
    scmsign = {
        'username': Username,
        'email': Email,
        'password': pw,  # Store the hashed password
    }

    user_cred.insert_one(scmsign)
    error_message="Succesully Registered"
    return html.TemplateResponse("signup.html", {"request": request, "error_message": error_message })
