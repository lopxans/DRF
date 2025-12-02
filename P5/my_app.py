import requests
import json

# URL = "http://127.0.0.1:8000/stu-api/"

URL = "http://127.0.0.1:8000/stu-validate-api/"  # Validate

# Read data  -----------------------------------------------
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()

    print(data)

# get_data()


# Create data -----------------------------------------------
def post_data():
    data = {
        'name': 'Selin Maharjan',
        'roll': 102,
        'city': 'Kuwait',
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    data = r.json()
    print(data)
    
# post_data()


# Update data -----------------------------------------------
def update_data():
    data = {
        'id': 1,
        'name': 'Sulav',
        'roll': 101,
        'city': 'Kathmandu',
    }
    
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    
    data = r.json()
    print(data)
    
update_data()

# Delete data -----------------------------------------------
def delete_data():
    data = {'id': 1}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    
    data = r.json()
    print(data)
    
# delete_data()