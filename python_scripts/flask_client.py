import requests, json

res = requests.get("http://localhost:1234/test_get", params={"num1":'24', "num2":'36'})
json_res = res.json()

for k,v in json_res.items():
    print(k,v)

res = requests.post("http://localhost:1234/test_post", data={"num1":'24', "num2":'36'})
json_res = res.json()

for k,v in json_res.items():
    print(k,v)
