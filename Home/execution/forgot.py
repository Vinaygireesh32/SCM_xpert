import re
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from execute.execute import user_cred


web = APIRouter()

html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

password_pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

f="forgot.html"

@web.get("/forgot")
def forgot(details: Request):
    return html.TemplateResponse(f, {"request": details, "error_message": None})

@web.post("/forgot")
def reset_password(request: Request, email: str = Form(...), username: str = Form(), password: str = Form(), confirm_password: str = Form()):
    # Validate email
    if not email_pattern.match(email):
        error_message = "Invalid email format"
        return html.TemplateResponse(f, {"request": request, "error_message": error_message})

    # Check if passwords match
    if password != confirm_password:
        error_message = "Passwords don't match"
        return html.TemplateResponse(f, {"request": request, "error_message": error_message})

    # Validate password
    if not password_pattern.match(password):
        error_message = "Password doesn't match the expectations"
        return html.TemplateResponse(f, {"request": request, "error_message": error_message})

    # Check if the provided username corresponds to the given email
    user = user_cred.find_one({"email": email, "username": username})

    if not user:
        # If no user is found with the provided email and username combination
        error_message = "User not found or invalid username/email combination"
        return html.TemplateResponse(f, {"request": request, "error_message": error_message})

    # Hash the new password using passlib
    hashed_password = pwd_cxt.hash(password)

    # Update the password in the user_cred collection based on the username and email
    result = user_cred.update_one({"email": email, "username": username}, {"$set": {"password": hashed_password}})

    if result.modified_count == 0:
        # If no document is modified, there was an issue updating the password
        error_message = "Failed to update password"
        return html.TemplateResponse(f, {"request": request, "error_message": error_message})

    success_message = "Password successfully reset"
    return html.TemplateResponse(f, {"request": request, "success_message": success_message})
