import requests

url = "https://ru.yougile.com/api-v2/auth/keys"

creds = {
    "login": "",
    "password": "",
    "companyId": "f16a00a0-31f4-47e1-800e-3f517a8e5c2b"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

responce = requests.post(url, json=creds, headers=headers)

token = responce.json().get("key")
print(f"Токен: {token}")