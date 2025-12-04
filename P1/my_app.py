import requests
url = "http://127.0.0.1:8000/1"

r = requests.get(url=url)
data = r.json()
print(data)