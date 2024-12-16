import requests

def get_token():
    url = "https://ru.yougile.com/api-v2/auth/keys"

    creds = {
        "login": "alekseeva151283@gmail.com",
        "password": "15121501Nem",
        "companyId": "f16a00a0-31f4-47e1-800e-3f517a8e5c2b"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=creds, headers=headers)

    return str(response.json().get("key"))
