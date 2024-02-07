from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import device_data
from execution.login import JSONResponse
from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.security import OAuth2PasswordBearer

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@web.get("/devicedata")
def details(request : Request):
    return html.TemplateResponse("devicedata.html", {"request": request})


# Route to get device data based on Device_ID
@web.post("/devicedata")
async def get_device_data(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        if token:
            dev = await request.json()
            device_id = dev.get("Device_ID")
            if device_id:
                # Assuming you want to filter data based on the received device_id {"Device_ID": device_id}
                shipment = list(device_data.find({'Device_ID': int(device_id)}, {'_id': 0}))
                return JSONResponse(content={"data": shipment}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

  