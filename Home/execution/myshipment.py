from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from execution.login import *
from fastapi import Depends

web = APIRouter()

html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

@web.get("/myshipment")
def get_myshipment(request: Request):
    data = shipment_cred.find({}, {'id': 0}) 
    json_data = list(data)
    return html.TemplateResponse("myshipment.html", {"request": request, "myship": json_data})


