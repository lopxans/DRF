import requests
import json


URL = "http://127.0.0.1:8000/"  

# Read data  -----------------------------------------------
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()

    print(data)

# get_data()


# Create data -----------------------------------------------
def post_data():
    data = {
        'name': 'Ram',
        'roll': 104,
        'city': 'Delli',
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)

    data = r.json()
    print(data)
    
# post_data()


# Update data -----------------------------------------------
def update_data():
    data = {
        'id': 4,
        'name': 'Ram Bahadur',
        'roll': 104,
        'city': 'Pokhara',
    }
    
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    
    data = r.json()
    print(data)
    
# update_data()

# Delete data -----------------------------------------------
def delete_data():
    data = {'id': 4}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers , data=json_data)
    
    data = r.json()
    print(data)
    
delete_data()