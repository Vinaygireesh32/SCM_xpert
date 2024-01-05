from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from execute.execute import *
from execution.login import*

web = APIRouter()

html = Jinja2Templates(directory = "html")
web.mount("/static", StaticFiles(directory="static"), name = "static")

@web.get("/newshipment")
def NewShipment(newdata : Request):
    return html.TemplateResponse("newshipment.html", {"request": newdata})

@web.post("/newshipment")
def NewShipment(request : Request, shipment_num  : str = Form(), container_num : str = Form(),route_details: str = Form(),goods_type: str = Form(),device: str = Form(),expected_delivery_date: str = Form(),po_num: str = Form(),delivery_num: str = Form(),ndc_num: str = Form(),batch_id: str = Form(),serial_num: str = Form(),description: str = Form()):
    scmdb ={
        'shipmentnumber': shipment_num,
        'containerumber': container_num,
        'routedetails'  : route_details,
        'goodstype'     : goods_type,
        'device'        : device,
        'expecteddeliverydate': expected_delivery_date,
        'ponumber'      : po_num,
        'deliverynumber': delivery_num,
        'ndcnumber'     : ndc_num,
        'batchid'       : batch_id,
        'serialnumberofgoods': serial_num,
        'shipmentdescription': description    
    }
    shipment_cred.insert_one(scmdb)
    return html.TemplateResponse("newshipment.html", {"request": request})