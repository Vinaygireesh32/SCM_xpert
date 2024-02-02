from confluent_kafka import Consumer
import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
mongodb_connection_string = os.getenv('MONGODB_CONNECTION_STRING')
mongodb_database_name = os.getenv('MONGODB_DATABASE_NAME')
User = MongoClient('mongodb+srv://vinaygireesh2001:7Ou9h3TZz9YZ4E6V@cluster0.8nikeyx.mongodb.net/')
DB = User['scm_xpert']
device_data = DB['DeviceData']

# Kafka configuration
config = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
    'group.id': os.getenv('KAFKA_GROUP_ID'),
    'enable.auto.commit': os.getenv('KAFKA_ENABLE_AUTO_COMMIT'),
    'auto.offset.reset': os.getenv('KAFKA_AUTO_OFFSET_RESET')
}

cust = Consumer(config)
topic = os.getenv('KAFKA_TOPIC')
cust.subscribe([topic])

try:
    while True:
        msg = cust.poll(1.0)
        if msg is None:
            pass
        elif msg.error():
            print("ERROR: {}".format(msg.error()))
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
