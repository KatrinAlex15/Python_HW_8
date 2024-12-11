import requests


url = "https://ru.yougile.com/api-v2/users"

headers = {
    "Autorization":"bearer i1u0et-EIVsVgwclqp4Ft-xnTMNn90EhrSnAbJso+c3UR2rzt-2WrJ2QhKi3FwhP",
    "Content-Type":"application/json"
}

responce = requests.get(url, headers=headers)

users_data = responce.json()
print("Инфо о сотрудниках: ", users_data)

users = users_data.get('content', [])

print("Список сотрудников: ")
for user in users:
    print(f"ID: {user['id']}, Имя: {user.get('realName')}")
