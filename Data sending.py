import time
import requests




temperature = [1, 2, 3, 5, 6, 7, 8]
humidity = [7, 3, 7, 5, 4, 2, 1]

for x in range(7):
    resp=requests.get('https://api.thingspeak.com/update?api_key=JKSMXUYL0QC1K64I&field1=%s&field2=%s' %(temperature[x], humidity[x]))
    time.sleep(10)
