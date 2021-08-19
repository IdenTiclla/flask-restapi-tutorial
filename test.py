import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "video/7", {"name":"moana","views": 1,"likes": 10})
print(response.json())
input()

# response = requests.get(BASE + "video/6", {"name":"moana","views": 1,"likes": 10})
# print(response.json())

response = requests.patch(BASE + "video/7", {"name":"moana 2","views": 2,"likes": 20})
print(response)