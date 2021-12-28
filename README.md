weatherPi

Weather station project on the raspberrypi

Directions below assume some basic knowledge of raspberryPi and command line

_________________________________________________________________________________________________________________________________________________________

Hardware required:

Raspberrypi 3b+ -       https://shop.pimoroni.com/products/raspberry-pi-3-b-plus
VEML7700 sensor -       https://shop.pimoroni.com/products/adafruit-veml7700-lux-sensor-i2c-light-sensor
BME280 sensor -         https://shop.pimoroni.com/products/bme280-breakout
Wind and rain sensors - https://shop.pimoroni.com/products/wind-and-rain-sensors-for-weather-station-wind-vane-anemometer-rain-gauge
RJ11 connectors -       https://shop.pimoroni.com/products/rj11-6-pin-connector
Breadboard -            https://shop.pimoroni.com/products/solderless-breadboard-400-point
Jumper leads -          https://shop.pimoroni.com/products/maker-essentials-mini-breadboards-jumper-jerky
4.7k resistor -         https://shop.pimoroni.com/products/e3-series-resistor-set-480pcs-10e-to-1m
T-Cobbler -             https://shop.pimoroni.com/products/adafruit-pi-t-cobbler-plus-kit-breakout-for-raspberry-pi-b
Ribbon Cable -          https://shop.pimoroni.com/products/gpio-ribbon-cable-for-raspberry-pi-model-a-b-40-pins?variant=12654559625299
MCP3008 -               https://shop.pimoroni.com/products/microchip-analog-to-digital-convertor?variant=373567061

Weatherproofing enclosures

Optional:
Camera -                https://shop.pimoroni.com/products/raspberry-pi-zero-camera-module?variant=40236918090

Note: You can also use a USB webcam

https://www.raspberrypi.com/documentation/computers/os.html#using-a-usb-webcam

_________________________________________________________________________________________________________________________________________________________

Installs required:

Your raspberryPi should be set up with latest OS.
see instructions as follows:
https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system

Once installed run the following commands:

$ sudo raspi-config

This will bring you to the config screen

I suggest updating password

Also enable I2C and SPI, also camera if you are using a raspberryPi camera

set your locales

Also run update

Further instructions and advice here
https://www.raspberrypi.com/documentation/computers/configuration.html

Run a reboot once you have made changes

$ sudo reboot


Once above complete with config run the following:

$ sudo apt-get update
$ sudo apt-get upgrade


Now run the following once update and upgrade complete.

$ sudo apt-get install python3-pip

https://www.raspberrypi.com/documentation/computers/os.html#installing-python-libraries


Libraries for the sensors:
$ pip3 install adafruit-circuitpython-veml7700
$ pip3 install adafruit-circuitpython-bme280

_________________________________________________________________________________________________________________________________________________________

Wiring:

See wiring.pdf for instructions of wiring. I have shown this without the use of the T-cobbler.
If using the T-cobbler please adjust as required

Additional support for MCP3008 wiring:
https://tutorials-raspberrypi.com/mcp3008-read-out-analog-signals-on-the-raspberry-pi/

Datasheet for the rain and wind sensors is also very important. Not just for wiring but also for calculations in the code.
https://cdn.shopify.com/s/files/1/0174/1800/files/windandrainsensors.pdf?v=1622723515

Images used to make wiring diagram:
https://pixabay.com/vectors/breadboard-arduino-technology-5659036/
https://pixabay.com/vectors/resistor-resistance-electronics-32290/
https://pinout.xyz/

_________________________________________________________________________________________________________________________________________________________

A lot of inspiration for my project was driven from tutorial provided on raspberrypi.org

https://projects.raspberrypi.org/en/projects/build-your-own-weather-station

This goes through alot of the concepts I have used in great detail, any variations will be noted in my scripts.

Also Adafruit give excellent example code for there sensor libraries and I adapted elements of my code from this

https://circuitpython.readthedocs.io/projects/bme280/en/2.6.7/examples.html#
https://circuitpython.readthedocs.io/projects/veml7700/en/latest/examples.html#

_________________________________________________________________________________________________________________________________________________________

Note: This project was done as part of an assignment in college for networking hence there is additional code to the raspberrypi.org example as in my
project the output of the weather station goes to a raspberrypi web server and also to the https://thingspeak.com/ interface.

Details of my webserver configuration can be found here:


Tutorials for using ThingSpeak can be found here:
https://uk.mathworks.com/help/thingspeak/getting-started-with-thingspeak.html

_________________________________________________________________________________________________________________________________________________________
