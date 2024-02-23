from fastapi import APIRouter, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



web = APIRouter()

html=Jinja2Templates(directory = "html")

web.mount("/static", StaticFiles(directory="static"), name="static")

@web.get("/dashboard")
def details(request: Request):
    return html.TemplateResponse("dashboard.html", { "request" : request})

