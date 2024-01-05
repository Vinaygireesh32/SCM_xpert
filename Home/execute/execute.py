import pymongo
 
MONGO_URI = 'mongodb://localhost:27017/'
 
User = pymongo.MongoClient(MONGO_URI)
 
DB = User ["scm_xpert"]
 
user_cred = DB["customers"]
 
shipment_cred = DB["NewShipment"]

admin_cred = DB["admin"]



