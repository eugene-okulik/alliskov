import pytest
import requests
import random
from faker import Faker

api_url = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope='session', autouse=True)
def inform_suite():
    print('Start testing')
    yield
    print('Testing complete')


@pytest.fixture(scope='function', autouse=True)
def inform_case():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def count_objects():
    response = requests.get(api_url)
    objects_quantity = len(response.json()['data'])
    return objects_quantity


@pytest.fixture()
def create_object():
    url = api_url
    body = {
        'name': str(Faker().state()),
        'data': {
            'address': str(Faker().address()),
            'birthdate': str(Faker().past_date()),
            'mail': str(Faker().email()),
            'name': f'{Faker().first_name()} {Faker().last_name()}',
            'sex': random.choice(['M', 'F']),
            'username': str(Faker().user_name())
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
    object_id = response.json()['id']
    yield body, response
    requests.delete(f'{api_url}/{object_id}')


@pytest.mark.medium
def test_get_all_objects(count_objects, create_object):
    response = requests.get(api_url)
    assert response.status_code == 200, \
        f'Returned status code {response.status_code} while expected 200'
    assert len(response.json()['data']) == count_objects + 1, \
        f'Returned objects number {len(response.json()["data"])} while expected {count_objects + 1}'


def test_get_object_by_id(create_object):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    get_response = requests.get(f'{api_url}/{new_object_id}')
    assert get_response.status_code == 200, \
        f'Returned status code {get_response.status_code} while expected 200'
    assert get_response.json()['id'] == new_object_id, \
        f'Returned object ID {get_response.json()["id"]} while expected {new_object_id}'
    assert get_response.json()['data']['name'] == create_body['data']['name'], \
        f'Returned name {get_response.json()["data"]["name"]} while expected {create_body["data"]["name"]}'


@pytest.mark.parametrize('iteration', range(3))
@pytest.mark.critical
def test_add_new_object(create_object, iteration):
    create_body, create_response = create_object
    assert create_response.status_code == 200, \
        f'Returned status code {create_response.status_code} while expected 200'
    assert create_response.json()['name'] == create_body['name'], \
        f'Returned city name {create_response.json()["name"]} while expected {create_body["name"]}'
    assert create_response.json()['data']['name'] == create_body['data']['name'], \
        f'Returned name {create_response.json()["data"]["name"]} while expected {create_body["data"]["name"]}'


def test_put_update_object(create_object):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    url = f'{api_url}/{new_object_id}'
    body = {
        'name': 'Old Mexico',
        'data': create_body['data']
    }
    headers = {
        'Content-Type': 'application/json'
    }
    put_response = requests.put(
        url=url,
        json=body,
        headers=headers
    )
    assert put_response.status_code == 200, \
        f'Returned status code {put_response.status_code} while expected 200'
    assert str(put_response.json()['id']) == str(new_object_id), \
        f'Returned object ID {put_response.json()["id"]} while expected {new_object_id})'
    assert put_response.json()['name'] == 'Old Mexico', \
        f'Returned address {put_response.json()["data"]["address"]} while expected Old Mexico'
    assert put_response.json()['data'] == create_body['data'], \
        f'Returned data object {put_response.json()["data"]} while expected {create_body["data"]}'


@pytest.mark.parametrize('name', ['Old York', 'Eldorado', 'Mushmore'])
def test_patch_update_object(create_object, name):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    url = f'{api_url}/{new_object_id}'
    body = {
        'name': name
    }
    headers = {
        'Content-Type': 'application/json'
    }
    patch_response = requests.patch(
        url=url,
        json=body,
        headers=headers
    )
    assert patch_response.status_code == 200, \
        f'Returned status code {patch_response.status_code} while expected 200'
    assert str(patch_response.json()['id']) == str(new_object_id), \
        f'Returned object ID {patch_response.json()["id"]} while expected {new_object_id})'
    assert patch_response.json()['name'] == name, \
        f'Returned mail {patch_response.json()["name"]} while expected {name}'
    assert len(patch_response.json()['data']) == 6, \
        f'Returned {len(patch_response.json()["data"])} elements in "data" object while expected 6'
    assert patch_response.json()['data']['mail'] == create_body['data']['mail'], \
        f'Returned mail {patch_response.json()["data"]["mail"]} while expected {create_body["data"]["mail"]}'


def test_delete_object(create_object):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    url = f'{api_url}/{new_object_id}'
    delete_response = requests.delete(url)
    get_object_by_id = requests.get(url)
    assert delete_response.status_code == 200, \
        f'Returned status code {delete_response.status_code} while expected 200'
    assert delete_response.text == f'Object with id {str(new_object_id)} successfully deleted', \
        f'Returned id {delete_response.text.split()[3]} while expected {new_object_id}'
    assert get_object_by_id.status_code == 404, \
        f'Returned status coe {get_object_by_id.status_code} while expected 404'
