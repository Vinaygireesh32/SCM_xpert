from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import device_data,admin_cred  # Importing device_data from config.config module
from execution.login import JSONResponse, decode_token  # Importing JSONResponse from execution.login module
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

# Creating an APIRouter instance named "web"
web = APIRouter()

# Creating a Jinja2Templates instance for rendering HTML templates located in the "html" directory
html = Jinja2Templates(directory="html")

# Mounting a directory containing static files (e.g., CSS, JavaScript) to the "/static" path
web.mount("/static", StaticFiles(directory="static"), name="static")

# Creating an instance of OAuth2PasswordBearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Route to render the "devicedata.html" template
@web.get("/devicedata")
def details(request: Request):
    return html.TemplateResponse("devicedata.html", {"request": request})

# Route to handle POST requests for fetching device data based on Device_ID
@web.post("/devicedata")
async def get_device_data(request: Request, token: str = Depends(decode_token)):
    
    try:
        if token:
            if admin_cred.find_one({"username" : token["sub"]}):
                dev = await request.json()  # Parsing JSON data from the request body
                device_id = dev.get("Device_ID")  # Extracting the Device_ID from the parsed JSON data
                if device_id:
                    # Fetching device data from the device_data collection based on Device_ID
                    shipment = list(device_data.find({'Device_ID': int(device_id)}, {'_id': 0}))
                    return JSONResponse(content={"data": shipment}, status_code=200)  # Returning fetched data as JSON response
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)  # Handling exceptions and returning error response if any
