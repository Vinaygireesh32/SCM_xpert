from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execution.login import jwt  # Importing jwt from execution.login module
from config.config import shipment_cred, user_cred  # Importing shipment_cred from execute.execute module
from fastapi.security import OAuth2PasswordBearer

# Creating an APIRouter instance named "web"
web = APIRouter()

# Creating a Jinja2Templates instance for rendering HTML templates located in the "html" directory
html = Jinja2Templates(directory="html")

# Mounting a directory containing static files (e.g., CSS, JavaScript) to the "/static" path
web.mount("/static", StaticFiles(directory="static"), name="static")

# Creating an instance of OAuth2PasswordBearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Route to render the "myshipment.html" template
@web.get("/shipment")
def shipment_html(request: Request):
    return html.TemplateResponse("shipment.html", {"request": request})

# Route to fetch shipment data in JSON format
@web.get("/shipmenttable")
def shipment1(request: Request):
    try:
        # Decoding JWT token from request headers
        payload = jwt.decode(request.headers["authorization"][7:], "yourkey", algorithms="HS256")
        if payload:
            # Fetching shipment data based on the username in JWT payload
            ship_data = list(shipment_cred.find({},{"_id": 0}))
            if ship_data:
                return JSONResponse(content=ship_data, status_code=200)  # Returning fetched data as JSON response
        # Returning an HTTPException if shipments are not found
        return HTTPException(status_code=400, detail="Shipments Not Found")
    except HTTPException as http_error:
        # Handling HTTPException and returning error message as JSON response
        return JSONResponse(content={"error_message": http_error.detail})
