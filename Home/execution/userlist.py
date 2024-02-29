from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from config.config import *
from execution.login import *

web = APIRouter()

html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")

@web.get("/userlist")
def details(request: Request):
    return html.TemplateResponse("userlist.html", {"request": request})

@web.post("/userlist")
async def get_user_data(request: Request, token: str = Depends(decode_token)):
    try:

        if admin_cred.find_one({"username" : token["sub"]}):
            data = await request.json()
            username = data.get("username")
            if not username:
                return JSONResponse(content={"data": "Username Required*"}, status_code=400)
            users = list(user_cred.find({'username': str(username)}, {'_id': 0}))

            if users:
                return JSONResponse(content={"data": users}, status_code=200)
            return JSONResponse(content={"data": "User not Found"}, status_code=400)
    except Exception as e:

        return JSONResponse(content={"error": str(e)}, status_code=500)

@web.post("/make_admin")
async def make_users_admin(request: Request, token: str = Depends(decode_token)):
    try:
         if admin_cred.find_one({"username" : token["sub"]}):
            data = await request.json()

            if data and "usernames" in data:
                success_messages = []

                for username in data["usernames"]:
                    user = user_cred.find_one({"username": username}, {'_id': 0})
                    if user:
                        # Move user from user_cred to admin_cred
                        user_cred.delete_one({"username": user["username"]})
                        admin_cred.insert_one(user)

                        success_messages.append(f"User '{username}' made admin successfully")

                return JSONResponse(content={"success": success_messages}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
