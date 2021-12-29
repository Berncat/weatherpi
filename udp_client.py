import socket
import logging
from dotenv import dotenv_values

# load configuration values from .env file
config = dotenv_values(".env")

logging.basicConfig(level=logging.INFO)

# UDP Client configuration parameters
serverAddressPort = (config["ipAddress"], int(config["udpport"]))
deviceID = config["deviceID"]
interval = int(config["transmissionInterval"])

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

logging.info(f"Listening for UDP Datagrams on port: {serverAddressPort}")


def udp(message):
    msgFromClient = message
    bytesToSend = str(msgFromClient).encode()
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    # Log to console:
    logging.info("Sent to server: " + str(msgFromClient))