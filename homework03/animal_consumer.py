import json
import requests

def getdata():
    with open("animals.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata

test= getdata();
print(type(test))

response1 = requests.get(url="http://localhost:5003/animals")
response2 = requests.get(url="http://localhost:5003/animals/head/?name=bunny")
response3 = requests.get(url="http://localhost:5003/animals/legs/?number=6")

print(response1.content)
print(response2.content)
print(response3.content)
