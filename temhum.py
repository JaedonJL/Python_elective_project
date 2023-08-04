import Adafruit_DHT
import requests
import time


sensor = Adafruit_DHT.AM2302
pin = 5

while (1):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        resp = req.get('https://api.thingspeak.com/update?api_key=R6J56QOW5UG7ALMV&field1=%s&field2=%s' % (temperature, humidity))
    else:
        print("Failed to get reading, will try again")
    sleep(2)