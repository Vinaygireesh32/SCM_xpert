from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from execution.login import*

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/signup")
def Signup(signdata : Request):
    return html.TemplateResponse("signup.html", {"request": signdata})

@web.post("/signup")
def Signup(request: Request, Username : str = Form(), Email : str = Form(), Create_Password : str = Form(), Confirm_Password : str = Form()):
    scmsign={
        'username' : Username,
        'email' : Email,
        'password' : Create_Password,
        'confirmpassword' : Confirm_Password
    }
    user_cred.insert_one(scmsign)
    return html.TemplateResponse("signup.html", {"request": request})