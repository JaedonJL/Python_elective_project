import Adafruit_DHT
import requests as req
from hal_temp_humidity_sensor import read_temp_humidity as read


sensor = Adafruit_DHT.AM2302
pin = 22

while (1):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        resp = req.get('https://api.thingspeak.com/update?api_key=R6J56QOW5UG7ALMV&field1=%s&field2=%s' % (temperature, humidity))
    else:
        print("Failed to get reading, will try again")


#import Adafruit_DHT
import requests as req

#def send_sensor_data_to_thingspeak(api_key, sensor_type=Adafruit_DHT.AM2302, pin=5):
#    while True:
#        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, pin)
#        if humidity is not None and temperature is not None:
#            url = f'https://api.thingspeak.com/update?api_key={api_key}&field1={temperature:.2f}&field2={humidity:.2f}'
#            resp = req.get(url)
#            print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
#       else:
#            print("Failed to get reading, will try again")

#send_sensor_data_to_thingspeak(api_key='R6J56QOW5UG7ALMV')


import time

import RPi.GPIO as GPIO

from . import dht11

def init():
    GPIO.setmode(GPIO.BCM)
    global dht11_inst

    dht11_inst = dht11.DHT11(pin=21)  # read data using pin 21

def read_temp_humidity():

    global dht11_inst

    ret = [-100, -100]

    result = dht11_inst.read()

    if result.is_valid():
        #print("Temperature: %-3.1f C" % result.temperature)
        #print("Humidity: %-3.1f %%" % result.humidity)

        ret[0] = result.temperature
        ret[1] = result.humidity

    return ret