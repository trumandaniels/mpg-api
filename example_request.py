import requests

BASE_URL = "http://127.0.0.1:5000/" #the URL of the server, in this case localhost

data = {
            "cylinders":6,
            "displacement":300,
            "horsepower":150,
            "weight":3000,
            "acceleration":10,
            "modelyear":85,
            "origin":"American",
        }

response = requests.post(BASE_URL, json=data) #note this is a post request
print(response.json())
 
