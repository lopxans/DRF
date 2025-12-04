import requests
import json
url = "http://127.0.0.1:8000/"


data = {
    'name': 'Ram Tamang',
    'roll': 4,
    'city': 'khai',
}
json_data = json.dumps(data)
r = requests.post(url=url, data=json_data)
data = r.json()
print(data)