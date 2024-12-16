import requests


url = "https://ru.yougile.com/api-v2/users"

headers = {
    "Autorization":"Bearer QsIacjPnlQvkMIFbuwGFXme-DmTTN-PRAsjSvvD5QRPGY+ey2X3nbfOWSiLB8xPs",
    "Content-Type":"application/json"
}

response = requests.get(url, headers=headers)

users_data = response.json()
print("Инфо о сотрудниках: ", users_data)

users = users_data.get('content', [])

print("Список сотрудников: ")
for user in users:
    print(f"ID: {user['id']}, Имя: {user.get('realName')}")
