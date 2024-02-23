from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

web = APIRouter()

html = Jinja2Templates(directory = "html") #Initialization of Jinja2Templates
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/about")
def details(details : Request):
    return html.TemplateResponse("about.html", {"request": details})
