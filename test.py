import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/5", {"name":"moana","views": 1,"likes": 10})
print(response.json())
input()

# response = requests.get(BASE + "video/6", {"name":"moana","views": 1,"likes": 10})
# print(response.json())

response = requests.get(BASE + "video/5")
print(response)