import socket
from confluent_kafka import Producer
import socket
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
host=os.getenv('host')
port=os.getenv('port')
bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")
topic_name = os.getenv("TOPIC_NAME")

soc = socket.socket()
connected = True
soc.connect((host, int(port)))

config = {'bootstrap.servers': bootstrap_servers}

producer = Producer(config)

while connected:
    message = soc.recv(1024).decode("utf-8")
    print(message)
    producer.produce(topic_name, key="key", value=message)
