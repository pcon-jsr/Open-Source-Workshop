import requests, json

res = requests.get("https://api.exchangeratesapi.io/latest", params={"base":'USD'})
json_res = res.json()

print(res.status_code)

for k,v in json_res['rates'].items():
    print(k,v)
