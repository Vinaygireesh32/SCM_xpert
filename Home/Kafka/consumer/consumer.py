from confluent_kafka import Consumer
from configparser import ConfigParser
from confluent_kafka import Consumer, OFFSET_BEGINNING
 
import json
from pymongo import MongoClient
 
# Connect to MongoDB
User = MongoClient('mongodb+srv://vinaygireesh2001:7Ou9h3TZz9YZ4E6V@cluster0.8nikeyx.mongodb.net/')  # Replace with your MongoDB connection string
DB = User['scm_xpert']  # Replace with your MongoDB database name
device_data = DB['DeviceData']  
config = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'foo',
        'enable.auto.commit': 'false',
        'auto.offset.reset': 'earliest'}
 

cust = Consumer(config)
topic = "topic"
cust.subscribe([topic])
try:
    while True:
        msg = cust.poll(1.0)
        if msg is None:
            pass
        elif msg.error():
            print("ERROR: %s".format(msg.error()))
        else:
            print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
            device_data.insert_one(json.loads(msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
        # Leave group and commit final offsets
        cust.close()
 
print(cust)