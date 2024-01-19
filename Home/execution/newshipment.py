from fastapi import APIRouter,Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from execution.login import*
from pydantic import BaseModel

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



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



@web.get("/newshipment")
def NewShipment(newdata : Request):
    return html.TemplateResponse("newshipment.html", {"request": newdata})

@web.post("/newshipment")
def NewShipment(request: Request, newship : Newshipment, token: str = Depends(oauth2_scheme)):
    scmdb ={
        # "email"         : token["email"],
        "shipmentnumber": newship.shipment_num,
        "containerumber": newship.container_num,
        "routedetails"  : newship.route_details,
        "goodstype"     : newship.goods_type,
        "device"        : newship.device,
        "expecteddeliverydate": newship.expected_delivery_date, 
        "ponumber"      : newship.po_num,
        "deliverynumber": newship.delivery_num,
        "ndcnumber"     : newship.ndc_num,
        "batchid"       : newship.batch_id,
        "serialnumberofgoods": newship.serial_num,
        "shipmentdescription": newship.description
    }
    
    shipment_cred.insert_one(scmdb)