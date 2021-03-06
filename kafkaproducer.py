import json
import time
import urllib.request
from kafka.errors import KafkaError
from kafka import KafkaProducer

API_KEY = "65beeafb8527ee3d2c9bca1ac7ee195f194f7001" # FIXME Set your own API key here
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        producer.send("velib-stations", json.dumps(station).encode())#.add_callback(on_send_success).add_errback(on_send_error)
    print("{} Produced {} station records".format(time.time(), len(stations)))
    print(json.dumps(station).encode())
    time.sleep(1)