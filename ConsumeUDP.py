import requests
import json

URL = ""
RequestTime = ""

response = requests.get(URL + "/" + RequestTime)
print(response)

