from pprint import pprint

import requests
import json

url = "http://httpbin.org/post"

payload = json.dumps({
    "nume": "Hustiuc",
    "prenume": "Andrei",
    "email": "andreihustiuc@yahoo.com"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.content)
json_response = response.json()
pprint(json_response)

for key, value in json_response.items():
    print(key, value)


#todo :