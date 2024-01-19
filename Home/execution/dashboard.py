from fastapi import APIRouter, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from execute.execute import *
from execution.login import *


web = APIRouter()

html=Jinja2Templates(directory = "html")

web.mount("/static", StaticFiles(directory="static"), name="static")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

@web.get("/dashboard")
def details(request: Request):

    return html.TemplateResponse("dashboard.html", { "request" : request})