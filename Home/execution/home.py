from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import shipment_cred


web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/")
def details(details : Request):
    data = shipment_cred.find()
    return html.TemplateResponse("home.html", {"request": details, "home": data})
