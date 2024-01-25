import pymongo
 
MONGO_URI = 'mongodb+srv://vinaygireesh2001:7Ou9h3TZz9YZ4E6V@cluster0.8nikeyx.mongodb.net/'
 
User = pymongo.MongoClient(MONGO_URI)
 
DB = User ["scm_xpert"]
 
user_cred = DB["customers"]
 
shipment_cred = DB["NewShipment"]

admin_cred = DB["admin"]

device_data = DB["DeviceData"]



