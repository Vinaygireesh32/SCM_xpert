from pydantic import BaseModel

# Define a Pydantic model for the new shipment data
class Newshipment(BaseModel):
    shipment_num: int
    container_num: int
    route_details: str
    goods_type: str
    device: int
    expected_delivery_date: str
    po_num: int
    delivery_num: int
    ndc_num: int
    batch_id: int
    serial_num: int
    description: str


class Sign(BaseModel):
    username: str
    email: str
    password: str
