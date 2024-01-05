from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from execution.login import*

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/myshipment")
def details(details : Request):
    data = shipment_cred.find()
    return html.TemplateResponse("myshipment.html", {"request": details, "myship": data})

