import socket
from confluent_kafka import Producer
import socket
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")
topic_name = os.getenv("TOPIC_NAME")

config = {'bootstrap.servers': bootstrap_servers}

producer = Producer(config)

soc = socket.socket()
connected = True
soc.connect(("127.0.0.1", 1235))

while connected:
    message = soc.recv(1024).decode("utf-8")
    print(message)
    producer.produce(topic_name, key="key", value=message)
