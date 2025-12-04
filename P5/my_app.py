import requests
import json
url = "http://127.0.0.1:8000/"


# Read and Reatriev Data ---------------------------------------------------------
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
        
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)
# get_data()


# Create Data  ---------------------------------------------------------
def post_data():
    data = {
        'name': 'R',
        'roll': 5,
        'city': 'Dulikhel'
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)
post_data()


# Update Data  ---------------------------------------------------------
def update_data():
    data = {
        'id': 4,
        'name': 'Ram Bahadur Thapa',
        'city': 'Bhaktapur',
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)
# update_data()


# Update Data  ---------------------------------------------------------
def delete_data():
    data = {'id': 4}
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)
# delete_data()