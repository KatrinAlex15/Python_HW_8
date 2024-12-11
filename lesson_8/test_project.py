import requests

base_url = "https://ru.yougile.com/api-v2/"
user_token = "i1u0et-EIVsVgwclqp4Ft-xnTMNn90EhrSnAbJso+c3UR2rzt-2WrJ2QhKi3FwhP"

headers = {
    "Autirization": f"Bearer {user_token}",
    "Content-Type": "application/json"
    }

def create_project(title):
    data = {"title": title}
    responce = requests.post(base_url + 'projects', json=data, headers=headers)
    assert responce.status_code ==201
    print ("Проект создан")
    project_id = responce.json().get('id')
    return project_id

def test_create_project():
    data = {"title":"Проект дз"}
    responce = requests.post(base_url+'projects', json=data, headers=headers)
    assert responce.status_code == 201
    print("Проект создан")

def test_get_project():
    responce = requests.get(base_url+'projects', headers=headers)
    assert responce.status_code ==200
    print("Проекты получены")

def get_project_by_id():
    test_projeci_id = create_project("Проект дз")
    responce = requests.get(base_url+f'projects/{test_projeci_id}', headers=headers)
    assert responce.status_code == 200

def test_change_project():
    test_project_id = create_project("Проект PUT")
    data = {"title": "Проект с изменениями"}
    responce = requests.put(base_url + f'projects/{test_project_id}', json=data, headers=headers)
    assert responce.status_code == 200
    print("Проект изменен")

def test_create_project_without_title():
    data = {"description": "Проект без названия"}
    responce = requests.post(base_url+'projects', json=data, headers=headers)
    assert responce.status_code == 400

def test_get_project_by_invalid_id():
    responce = requests.get(base_url + 'projects/f16a00a0-31f4-47e1-800e-3f517a8e5c2bdd', headers=headers)
    assert responce.status_code == 404

def test_change_invalid_project():
    data = {"title": "Проект с изменениями"}
    responce = requests.put(base_url + f'projects/f16a00a0-31f4-47e1-800e-3f517a8e5c2bdd', json=data, headers=headers)
    assert responce.status_code == 404
