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
from udp_client import udp

# General variables required
stop = False  # keeps track of programme running
output = {}  # final output as a dict object

# Create I2C instances
i2c = board.I2C()
veml7700 = adafruit_veml7700.VEML7700(i2c, address=0x10)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Create weather vane instance using wind_direction class created at wind_direction.py
weather_vane = wind_direction()

# Now to create instances of the anemometer and rain gauge
# I have connected my anemometer at GPIO 16
# I have connected my rain gauge at GPIO 23
anemometer = Button(16)
rain_gauge = Button(23)

# need to create some global variables and functions to keep track of the anemometer and rain count
wind_pulse_count = 0
rain_pulse_count = 0


def wind_spins():
    global wind_pulse_count
    wind_pulse_count += 1


def rain_tipped():
    global rain_pulse_count
    rain_pulse_count += 1


def wind_result():
    global wind_pulse_count
    # convert to km/h per product datasheet
    result = (wind_pulse_count / 60) * 2.4
    wind_pulse_count = 0  # reset counter
    return result


def rain_result():
    global rain_pulse_count
    result = rain_pulse_count * 0.2794  # tippinig value in mm per product datasheet
    rain_pulse_count = 0  # reset counter
    return result


# lastly set property of GPIO pin so that when_pressed it increases count
anemometer.when_pressed = wind_spins
rain_gauge.when_pressed = rain_tipped

# Using lists to capture data
temperature_readings = []
humidity_readings = []
pressure_readings = []
lux_readings = []
vane_readings = []
wind_readings = []
rain_readings = []

# This is the function which willcollect the reading every 60 seconds and append to a list
def get_data():
    # This is to burn the first few readings from the sensors as first readings can be inaccurate
    for _ in range(5):
        bme280.temperature
        bme280.humidity
        bme280.pressure
        veml7700.light
    # Add readings to list
    temperature_readings.append(bme280.temperature)
    humidity_readings.append(bme280.humidity)
    pressure_readings.append(bme280.pressure)
    lux_readings.append(veml7700.light)
    vane_readings.append(weather_vane.get_direction())
    wind_readings.append(wind_result())
    rain_readings.append(rain_result())
    print('1 minute reading:', time.strftime("%H:%M:%S", time.gmtime()))

# This function gets the average of the lists for the main 15 minute output
def get_average():
    output.update(
        _id=time.strftime("%H:%M", time.gmtime()),
        date=time.strftime("%a %d %b %Y", time.gmtime()),
        temperature=round(statistics.mean(temperature_readings), 2),
        humidity=round(statistics.mean(humidity_readings), 2),
        pressure=round(statistics.mean(pressure_readings), 2),
        lux=round(statistics.mean(lux_readings), 2),
        wind_dir=statistics.mode(vane_readings),
        wind_speed=round(statistics.mean(wind_readings), 2),
        rainfall_period=round(statistics.mean(rain_readings), 2),
        rainfall_per_hour=round((statistics.mean(rain_readings) / 900)*3600, 2)
    )

# This function clears all the lists
def clear_readings():
    temperature_readings.clear()
    humidity_readings.clear()
    pressure_readings.clear()
    lux_readings.clear()
    vane_readings.clear()
    wind_readings.clear()
    rain_readings.clear()

# This function is to create a list file which can then be accessed by the thingspeak script to update thingspeak
def thingspeak():
    list_file = open("list.py", "w")

    thingspeak_list = [
        output.get('temperature'),
        output.get('humidity'),
        output.get('pressure'),
        output.get('lux'),
        output.get('wind_speed'),
        output.get('rainfall_period'),
    ]

    list_file = open("list.py", "w")
    for element in thingspeak_list:
        list_file.write(str(element) + "\n")
    list_file.close()


# main function
if __name__ == '__main__':
    time.sleep(60)
    # check is used to make sure that not more then one reading is done in a minute time section
    check = 0
    print('start: ', time.strftime("%H:%M:%S", time.gmtime()))
    while stop == False:
        # every minute take a reading
        if time.gmtime().tm_min % 1 == 0 and check != 1:
            get_data()
            check = 1
        # every 15 minutes average the readings and create an output
        if time.gmtime().tm_min % 15 == 0 and check != 2:
            get_average()
            print(output)
            udp(output)
            thingspeak()
            # this subprocess takes a picture from the webcam
            subprocess.run('/home/pi/weatherpi/photo.sh')
            check = 2
        # if an hour has passed shut down programme, cron job will restart it
        if time.gmtime().tm_min == 0:
            stop = True
            check = 0
            print('end:', time.strftime("%H:%M:%S", time.gmtime()))
        # if not zero it means a readings has been processed so sleep for 60 seconds
        if check != 0:
            time.sleep(60)
            check = 0
