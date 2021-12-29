import socket
from time import sleep
import logging
from dotenv import dotenv_values

#load configuration values from .env file
config = dotenv_values(".env")

logging.basicConfig(level=logging.INFO)

#TCP Client configuration parameters
serverAddressPort = (config["ipAddress"],int(config["tcpport"]))
deviceID = config["deviceID"]
interval = int(config["transmissionInterval"])

# create a socket object
socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 

# bind the socket object to the port
socket.connect(serverAddressPort)

logging.info(f"Connected to port: {serverAddressPort}")

file = open('/home/pi/weatherpi/image.jpg', "rb")
image = file.read(1024)

while image:
    print("sent")
    socket.sendall(image)
    image = file.read(1024)
    #Log to console:
logging.info("Sent to server")