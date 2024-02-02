from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execution.login import *
from execute.execute import *
from fastapi.security import OAuth2PasswordBearer
 
web=APIRouter()
html = Jinja2Templates(directory="html")
web.mount("/static", StaticFiles(directory="static"), name="static")
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = await  decode_token(token)
#     if payload and "sub" in payload and "email" in payload:
#         user_data = user_cred.find_one({"email": payload["email"]})
#         if user_data :
#             return user_data
 
@web.get("/myshipment")
def shipment_html(request: Request):
    return html.TemplateResponse("MyShipment.html", {"request": request})
 
@web.get("/myshipmenttable")
def shipment1(request: Request):
    
    try:
        payload = jwt.decode(request.headers["authorization"][7:], "yourkey", algorithms="HS256")
        if payload:
            ship_data = list(shipment_cred.find({"username" : payload["sub"]},{"_id":0}))
            if ship_data:
                return JSONResponse(content=ship_data,status_code=200)
        return HTTPException(status_code=400, detail="Shipments Not Found")
            
    except HTTPException as http_error:
            return JSONResponse(content={"error_message": http_error.detail})