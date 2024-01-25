from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from execution.login import *
from fastapi import Depends

# web = APIRouter()

# html = Jinja2Templates(directory="html")
# web.mount("/static", StaticFiles(directory="static"), name="static")

# @web.get("/myshipment")
# def get_myshipment(request: Request):
 
#     data = shipment_cred.find({}, {'id': 0}) 
#     json_data = list(data)
#     return html.TemplateResponse("myshipment.html", {"request": request, "myship": json_data})
 
web=APIRouter()
html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name="static")
 
 
# Assuming you have an oauth2_scheme defined like this:
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = decode_token(token)
#     # print(token)
#     if payload and "sub" in payload and "token" in payload:
#         user_data = user_cred.find_one({"username": payload["token"]})
#         # print(user_data)
#         if user_data :
#             return user_data
 
@web.get("/myshipment")
def shipment_html(request: Request):
    return html.TemplateResponse("myshipment.html", {"request": request})
 
@web.get("/myshipmentData")
def shipmentData(request: Request, token: str = Depends(oauth2_scheme)):
    print(token)
    try:
        payload=decode_token(token)
        # print(token)
        # a=decode_token(token)
        # print(a)
        if token:
            # print("token in shipment", a)
            ship = list(shipment_cred.find_one({"username" : payload["username"]},{"_id":0}))
            if ship:
            # return JSONResponse(content=ship_data, status_code=200)
                return JSONResponse(content=ship,status_code=200)
        return HTTPException(status_code=400, detail="Shipments Not Found")
            # return JSONResponse(content={"message": "Token is None"}, status_code=401)
    except HTTPException as http_error:
            return JSONResponse(content={"error_message": http_error.detail})