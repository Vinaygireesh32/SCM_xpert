import re
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from execute.execute import *
from execution.login import *

web = APIRouter()

html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

password_pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

@web.get("/forgot")
def forgot(details: Request):
    return html.TemplateResponse("forgot.html", {"request": details, "error_message": None})

@web.post("/forgot")
def reset_password(request: Request, email: str = Form(...), password: str = Form(), confirm_password: str = Form()):
    # Validate email
    if not email_pattern.match(email):
        error_message = "Invalid email format **"
        return html.TemplateResponse("forgot.html", {"request": request, "error_message": error_message})

    # Check if passwords match
    if password != confirm_password:
        error_message = "Passwords doesn't match"
        return html.TemplateResponse("forgot.html", {"request": request, "error_message": error_message})

    # Validate password
    if not password_pattern.match(password):
        error_message = "Password doesn't match the expectations"
        return html.TemplateResponse("forgot.html", {"request": request, "error_message": error_message})

    # Hash the new password using passlib
    hashed_password = pwd_cxt.hash(password)

    # Update the password in the user_cred collection
    result = user_cred.update_one({"email": email}, {"$set": {"password": hashed_password}})

    if result.modified_count == 0:
        # If no document is modified, the user with the provided email doesn't exist
        error_message = "User with this email not found"
        return html.TemplateResponse("forgot.html", {"request": request, "error_message": error_message})

    success_message = "Password successfully reset"
    return html.TemplateResponse("forgot.html", {"request": request, "success_message": success_message})
