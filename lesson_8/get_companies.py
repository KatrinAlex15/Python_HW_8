import requests

url = "https://ru.yougile.com/api-v2/auth/companies"

creds = {
    "login": "alekseeva151283@gmail.com",
    "password": "15121501Nem"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
response = requests.post(url, json=creds, headers=headers)

companies = response.json()
if isinstance(companies, list):
    print("Список компаний: ")
    for company in companies:
        print(f"ID:{company['id']}, Название: {company['name']}")
else:
    print("Найдена одна компания: ", companies)