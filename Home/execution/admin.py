from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/admin")
def admin(request : Request):
    return html.TemplateResponse("admin.html", { "request" : request})