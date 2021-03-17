from httplib2 import HTTPConnectionWithTimeout
import json
import random

Humidity = random.randrange(10, 40)
Temperature = random.randrange(10, 40)

# Sending the data to the server
headers = {"charset": "utf-8", "Content-Type": "application/json"}
conn = HTTPConnectionWithTimeout("127.0.0.1", 8000)
sample = {"sensor": "T2/H1", "measurement_type": "C", "humidity": Humidity, "temperature": Temperature}
sampleJson = json.dumps(sample, ensure_ascii='False')

conn.request("POST", "/rpi/", sampleJson, headers)
response = conn.getresponse()
print(response.read())
conn.close()
