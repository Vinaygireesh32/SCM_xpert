from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import shipment_cred


web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/about")
def details(details : Request):
    data = shipment_cred.find()
    return html.TemplateResponse("about.html", {"request": details, "about": data})
