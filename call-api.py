import requests

url = "http://localhost:8000/api"

headers = {
    "Authorization": "Token 2aee1daf64759e8bc2e2ff4d33606648f3010dfc",
    "Content-Type": "application/json"
}

payload = {
    "username": "admin",
    "password": "admin"
}

# ret = requests.post(url=url, json=payload, headers=headers)
ret = requests.get(url=url, headers=headers)

print(ret.json())