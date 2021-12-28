# *** Weather Station 2021 ***

# Code adapted from the following in some instances:
# @ https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/0
# @ https://circuitpython.readthedocs.io/projects/bme280/en/2.6.7/examples.html#
# @ https://circuitpython.readthedocs.io/projects/veml7700/en/latest/examples.html#

import board
import adafruit_veml7700
from adafruit_bme280 import basic as adafruit_bme280
from gpiozero import Button
from wind_direction import wind_direction
import time
import statistics
import subprocess

# General variables required
stop = False  # keeps track of programme running
output = {}  # final output as a dict object

# Create I2C instances
i2c = board.I2C()
veml7700 = adafruit_veml7700.VEML7700(i2c, address=0x10)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)