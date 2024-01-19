import socket
import errno
import json
import time
import random
import os
# from dotenv import load_dotenv
 
# load_dotenv()
 
 
# server = socket.gethostbyname(socket.gethostname()) #get Ip addr
# print(server)
ADDR = ("127.0.0.1", 12345)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT !"
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")
 
# bind this socket to the address we configured earlier
server.bind(("127.0.0.1", 1235))    
server.listen(2)
print(f"[LISTENING] Server is listening on {server}")
con, addr = server.accept()
print(f'CONNECTION FROM {ADDR} HAS BEEN ESTABLISHED')
connected = True
while connected:
        try:
            for i in range(0,5):
                route = ['Newyork,USA','Chennai, India','Bengaluru, India','London,UK']
                routefrom = random.choice(route)
                routeto = random.choice(route)
                if (routefrom!=routeto):
                    data = {
                        "Battery_Level":round(random.uniform(2.00,5.00),2),
                        "Device_ID": random.randint(1156053076,1156053078),
                        "First_Sensor_temperature":round(random.uniform(10,40.0),1),
                        "Route_From":routefrom,
                        "Route_To":routeto
                        }
                     # Convert dictionary to JSON format and encode it
                    userdata = (json.dumps(data, indent=1)).encode(FORMAT)  # Convert dictionary to JSON format and encode it
                    con.send(userdata)
                    print(userdata)
                    time.sleep(10)
                else:
                    continue
 
           
        except IOError as e:
            if e.errno == errno.EPIPE:
                pass
 
con.close()