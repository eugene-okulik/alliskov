import requests

host = 'http://167.172.172.115:52353'


def get_all_objects():
    url = f'{host}/object'
    response = requests.get(url)
    assert response.status_code == 200, \
        f'Returned status code {response.status_code} while expected 200'
    assert len(response.json()['data']) == 25, \
        f'Returned objects number {len(response.json()["data"])} while expected 25'
    return response


def get_object_by_id(object_id):
    url = f'{host}/object/{object_id}'
    response = requests.get(url)
    assert response.status_code == 200, \
        f'Returned status code {response.status_code} while expected 200'
    assert response.json()['id'] == object_id, \
        f'Returned object ID {response.json()["id"]} while expected {object_id}'
    return response


def add_new_object():
    url = f'{host}/object'
    body = {
        'name': 'Moderator',
        'data': {
            'address': '597 Manhattan Ave.Lawrence, MA 01841',
            'birthdate': '2000-01-02',
            'mail': 'dohnjoe@test.test',
            'name': 'Dohn Joe',
            'sex': 'M',
            'username': 'joe0901'
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        url=url,
        json=body,
        headers=headers
    )
    assert response.status_code == 200, \
        f'Returned status code {response.status_code} while expected 200'
    assert response.json()['name'] == 'Moderator', \
        f'Returned role {response.json()["name"]} while expected "Moderator"'
    assert response.json()['data']['name'] == 'Dohn Joe', \
        f'Returned name {response.json()["data"]["name"]} while expected "Dohn Joe"'
    return response


def put_update_object(object_id):
    url = f'{host}/object/{object_id}'
    body = {
        'name': 'Moderator',
        'data': {
            'address': '9419 W. Beach St.Tucson, AZ 85718',
            'birthdate': '2000-01-02',
            'mail': 'dohnjoe@test.test',
            'name': 'Dohn Joe',
            'sex': 'M',
            'username': 'joe0901'
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put(
        url=url,
        json=body,
        headers=headers
    )
    assert response.status_code == 200, \
        f'Returned status code {response.status_code} while expected 200'
    assert str(response.json()['id']) == str(object_id), \
        f'Returned object ID {response.json()["id"]} while expected {object_id})'
    assert type(response.json()['id']) == type(object_id), \
        f'Returned object ID type {type(response.json()["id"])} while expected {type(object_id)}'
    assert response.json()['data']['address'] == '9419 W. Beach St.Tucson, AZ 85718', \
        f'Returned address {response.json()["data"]["address"]} while expected "9419 W. Beach St.Tucson, AZ 85718"'
    delete_object(response.json()['id'])
    return response


def patch_update_object(object_id):
    url = f'{host}/object/{object_id}'
    body = {
        'data': {
            'mail': 'dohnjoe@com.com'
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.patch(
        url=url,
        json=body,
        headers=headers
    )
    assert response.status_code == 200, \
        f'Returned status code {response.status_code} while expected 200'
    assert str(response.json()['id']) == str(object_id), \
        f'Returned object ID {response.json()["id"]} while expected {object_id})'
    assert type(response.json()['id']) == type(object_id), \
        f'Returned object ID type {type(response.json()["id"])} while expected {type(object_id)}'
    assert response.json()['data']['mail'] == 'dohnjoe@com.com', \
        f'Returned mail {response.json()["data"]["mail"]} while expected "dohnjoe@com.com"'
    assert len(response.json()['data']) == 6, \
        f'Returned {len(response.json()["data"])} elements in "data" object while expected 6'
    delete_object(response.json()['id'])
    return response


def delete_object(object_id):
    url = f'{host}/object/{object_id}'
    response = requests.delete(url)
    assert response.status_code == 200, \
        f'Returned status code {response.status_code} while expected 200'
    assert response.text == f'Object with id {str(object_id)} successfully deleted', \
        f'Returned id {response.text.split()[3]} while expected {object_id}'
    return response


# Получение списка всех объектов
# print(get_all_objects().json())

# Получение одного объекта по id
# ids_list = []
# for obj in get_all_objects().json()['data']:
#     ids_list.append(obj['id'])
# print(get_object_by_id(random.choice(ids_list)).json())

# Добавление нового объекта
# new_object = add_new_object()
# print(new_object.json())
# object_id = new_object.json()['id']
# delete_object(object_id)


# Изменение существующего объекта PUT
# print(put_update_object(add_new_object().json()['id']).json())

# Изменение существующего объекта PATCH
# print(patch_update_object(add_new_object().json()['id']).json())

# Удаление объекта
# print(delete_object(add_new_object().json()['id']).text)
