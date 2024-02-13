from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execution.login import*

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/contact")
def details(details : Request):
    return html.TemplateResponse("contact.html", {"request": details})
