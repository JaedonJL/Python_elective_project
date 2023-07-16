import Adafruit_DHT


sensor = Adafruit_DHT.AM2302
pin = 5

while(1):
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)

    if humidity is not None and temperature is not None:
        print("temp = {0:.0.1f}*C Humidity={0.0:1f}%" .format(temperature,humidity))

    else:
        print("non")
