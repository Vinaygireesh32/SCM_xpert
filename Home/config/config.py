# Importing the pymongo library for interacting with MongoDB
import pymongo

# The MongoDB connection URI, which includes the username, password, host, and database name.
MONGO_URI = 'mongodb+srv://vinaygireesh2001:7Ou9h3TZz9YZ4E6V@cluster0.8nikeyx.mongodb.net/'

# Creating a MongoClient object to connect to the MongoDB server specified by the URI.
User = pymongo.MongoClient(MONGO_URI)

# Accessing the "scm_xpert" database from the MongoDB server.
DB = User ["scm_xpert"]

# Accessing the "customers" collection within the "scm_xpert" database.
user_cred = DB["customers"]

# Accessing the "NewShipment" collection within the "scm_xpert" database.
shipment_cred = DB["NewShipment"]

# Accessing the "admin" collection within the "scm_xpert" database.
admin_cred = DB["admin"]

# Accessing the "DeviceData" collection within the "scm_xpert" database.
device_data = DB["DeviceData"]

