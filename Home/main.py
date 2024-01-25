from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execution.login import web as log
from execution.signup import web as signup
from execution.newshipment import web as newship
from execution.myshipment import web as myship
from execution.admin import web as admin
from execution.about import web as about
from execution.contact import web as contact
from execution.home import web as home
from execution.forgot import web as forgot
from execution.devicedata import web as devicedata
from execution.dashboard import web as dashboard
from execution.myaccount import web as myaccount
from execution.adminacc import web as adminacc
from execution.userlist import web as userlist




app = FastAPI()
html = Jinja2Templates(directory = "html")
app.mount("/static", StaticFiles(directory="static"), name = "static")


app.include_router(log)
app.include_router(signup)
app.include_router(newship)
app.include_router(myship)
app.include_router(about)
app.include_router(contact)
app.include_router(forgot)
app.include_router(home)
app.include_router(admin)
app.include_router(devicedata)
app.include_router(dashboard)
app.include_router(myaccount)
app.include_router(adminacc)
app.include_router(userlist)