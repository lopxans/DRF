import requests
import json

URL = "http://127.0.0.1:8000/stu-api/"

# Read data  -----------------------------------------------
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()

    print(data)

# get_data()c


# Create data -----------------------------------------------
def post_data():
    data = {
        'name': 'Sulav Tamang',
        'roll': 10000,
        'city': 'Banepa Bazar',
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    data = r.json()
    print(data)
    
post_data()


# Update data -----------------------------------------------
def update_data():
    data = {
        'id': 3,
        'name': 'Priya Tamang',
        'roll': 300,
        'city': 'Kuwait',
    }
    
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    
    data = r.json()
    print(data)
    
# update_data()

# Delete data -----------------------------------------------
def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    
    data = r.json()
    print(data)
    
# delete_data()