from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import *  # Importing all items from execute.execute module
from execution.login import *  # Importing all items from execution.login module
from pydantic import BaseModel

# Creating an APIRouter instance named "web"
web = APIRouter()

# Creating a Jinja2Templates instance for rendering HTML templates located in the "html" directory
html = Jinja2Templates(directory="html")

# Mounting a directory containing static files (e.g., CSS, JavaScript) to the "/static" path
web.mount("/static", StaticFiles(directory="static"), name="static")

# Creating an instance of OAuth2PasswordBearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define a Pydantic model for the new shipment data
class Newshipment(BaseModel):
    shipment_num: str
    container_num: str
    route_details: str
    goods_type: str
    device: str
    expected_delivery_date: str
    po_num: str
    delivery_num: str
    ndc_num: str
    batch_id: str
    serial_num: str
    description: str

# Route to render the "newshipment.html" template
@web.get("/newshipment")
def new_shipment(newdata: Request):
    return html.TemplateResponse("newshipment.html", {"request": newdata, "token": "your_token_here"})

# Route to handle POST requests for adding new shipment data
@web.post("/newshipment")
def new_shipment(request: Request, new_ship: Newshipment, token: str = Depends(oauth2_scheme)):
    decode = decode_token(token)  # Decoding JWT token
    try:
        # Validate shipment number length
            if len(new_ship.shipment_num) != 7:
                raise HTTPException(status_code=400, detail="Shipment number must be exactly 7 digits")

        # Check if the shipment number already exists
            existing_shipment = shipment_cred.find_one({"shipmentnumber": new_ship.shipment_num})
            if existing_shipment is not None:
                raise HTTPException(status_code=400, detail="Shipment number already exists")

        # Creating a dictionary for storing new shipment data
            scmdb = {
                "username": decode["sub"],
                "shipmentnumber": new_ship.shipment_num,
                "containerumber": new_ship.container_num,
                "routedetails": new_ship.route_details,
                "goodstype": new_ship.goods_type,
                "device": new_ship.device,
                "expecteddeliverydate": new_ship.expected_delivery_date,
                "ponumber": new_ship.po_num,
                "deliverynumber": new_ship.delivery_num,
                "ndcnumber": new_ship.ndc_num,
                "batchid": new_ship.batch_id,
                "serialnumberofgoods": new_ship.serial_num,
                "shipmentdescription": new_ship.description
            }

            shipment_cred.insert_one(scmdb)  # Inserting new shipment data into the database
    except Exception:
        raise HTTPException(status_code=400, detail="user not found")