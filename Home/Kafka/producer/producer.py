import socket
from confluent_kafka import Producer
import socket
 
config = {'bootstrap.servers': 'localhost:9092'}
 
producer = Producer(config)
 
soc=socket.socket()
connected=True
soc.connect(("127.0.0.1",1235))
 
while connected:
    print(soc.recv(1024).decode("utf-8"))
    producer.produce("topic", key="key", value=soc.recv(1024).decode("utf-8"))
 