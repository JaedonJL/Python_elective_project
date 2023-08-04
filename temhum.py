import Adafruit_DHT
import requests as req



sensor = Adafruit_DHT.AM2302
pin = 5

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

# Replace 'YOUR_API_KEY' with your actual ThingSpeak API key
#send_sensor_data_to_thingspeak(api_key='YOUR_API_KEY')