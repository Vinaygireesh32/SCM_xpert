from pydantic import BaseModel

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


class Sign(BaseModel):
    username: str
    email: str
    password: str
