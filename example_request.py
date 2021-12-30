import requests

BASE_URL = "http://127.0.0.1:5000/"

# response = requests.get(BASE_URL + "helloworld/bill" )
response = requests.put(BASE_URL + "car/name", {"carname": "new_nickname_alert"})
print(response.json())
 
