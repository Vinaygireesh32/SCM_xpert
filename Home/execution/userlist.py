from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from execute.execute import *
from execution.login import *


web = APIRouter()

html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

@web.get("/userlist")
def details(request: Request):
    return html.TemplateResponse("userlist.html", {"request": request})

@web.post("/userlist")
async def get_user_data(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        if token:
            data = await request.json()
            username = data.get("username")
            if username:
                username = list(user_cred.find({'username': str(username)}, {'_id': 0}))
                return JSONResponse(content={"data": username}, status_code=200)
    except Exception as e:
        print("Error:", str(e))
        return JSONResponse(content={"error": str(e)}, status_code=500)

@web.post("/make_admin")
async def make_users_admin(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        if token:
            data = await request.json()
            if data and "usernames" in data:
                for username in data["usernames"]:
                    user = user_cred.find_one({"username": username}, {'_id': 0})
                    if user:
                        user_cred.delete_one({"username": user["username"]})
                        admin_cred.insert_one(user)
                return JSONResponse(content={"message": "Users made admin successfully"}, status_code=200)
            else:
                return JSONResponse(content={"error": "No user usernames provided"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
