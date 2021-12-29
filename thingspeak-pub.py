import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
import logging
from dotenv import dotenv_values

#load MQTT configuration values from .env file
config = dotenv_values(".env")

#configure Logging
logging.basicConfig(level=logging.INFO)

# Define event callbacks for MQTT
def on_connect(client, userdata, flags, rc):
    logging.info("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    logging.info("Message Sent ID: " + str(mid))

mqttc = mqtt.Client(client_id=config["clientId"])

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# parse mqtt url for connection details
url_str = sys.argv[1]
print(url_str)
url = urlparse(url_str)
base_topic = url.path[1:]

# Configure MQTT client with user name and password
mqttc.username_pw_set(config["username"], config["password"])
# Load CA certificate for Transport Layer Security
mqttc.tls_set("./broker.thingspeak.crt")

#Connect to MQTT Broker
mqttc.connect(url.hostname, url.port)
mqttc.loop_start()

#Set Thingspeak Channel to publish to
topic = "channels/"+config["channelId"]+"/publish"

payload=[]

list_file = open("list.py", "r")
for element in list_file:
    currentPlace = element[:-1]
    payload.append(currentPlace)
list_file.close()

print(payload)

# Publish a message
time.sleep(30)
try:
    payload1="field1="+str(payload[0])
    mqttc.publish(topic, payload1)
    time.sleep(int(config["interval"]))
    payload2="field2="+str(payload[1])
    mqttc.publish(topic, payload2)
    time.sleep(int(config["interval"]))
    payload3="field3="+str(payload[2])
    mqttc.publish(topic, payload3)
    time.sleep(int(config["interval"]))
    payload4="field4="+str(payload[3])
    mqttc.publish(topic, payload4)
    time.sleep(int(config["interval"]))
    payload5="field5="+str(payload[4])
    mqttc.publish(topic, payload5)
    time.sleep(int(config["interval"]))
    payload6="field6="+str(payload[5])
    mqttc.publish(topic, payload6)
    time.sleep(int(config["interval"]))
except:
    logging.info('Interrupted')