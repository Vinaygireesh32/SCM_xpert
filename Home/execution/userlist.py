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
                users = list(user_cred.find({'username': str(username)}, {'_id': 0}))
                print(users)
                if users:
                    return JSONResponse(content={"data": users}, status_code=200)
                return JSONResponse(content={"data": "no user found"}, status_code=400)
    except Exception as e:
        print("Error:", str(e))
        return JSONResponse(content={"error": str(e)}, status_code=500)


@web.post("/make_admin")
async def make_users_admin(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        if token:
            data = await request.json()
            print(data)
            if data and "usernames" in data:
                success_messages = []
                # error_messages = []

                for username in data["usernames"]:
                    user = user_cred.find_one({"username": username}, {'_id': 0})
                    if user:
                        user_cred.delete_one({"username": user["username"]})
                        admin_cred.insert_one(user)
                        success_messages.append(f"User '{username}' made admin successfully")
                        return JSONResponse(content={"success": success_messages}, status_code=200)
                   
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
   