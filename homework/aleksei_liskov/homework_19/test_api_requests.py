import pytest
import requests
import allure


@allure.suite('Objects API')
@allure.feature('Get objects')
@allure.story('Get all objects')
@allure.title('Get all objects')
@allure.severity('Critical')
@pytest.mark.regular
def test_get_all_objects(count_objects, create_object, api_url):
    with allure.step('Run GET request for all existing objects'):
        response = requests.get(api_url)
    with allure.step('Check that response status code is 200'):
        assert response.status_code == 200, \
            f'Returned status code {response.status_code} while expected 200'
    with allure.step('Check that number of the objects is correct'):
        assert len(response.json()['data']) == count_objects + 1, \
            f'Returned objects number {len(response.json()["data"])} while expected {count_objects + 1}'


@allure.suite('Objects API')
@allure.feature('Get objects')
@allure.story('Get object by ID')
@allure.title('Get by existing ID')
@allure.severity('Major')
def test_get_object_by_id(create_object, api_url):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    with allure.step(f'Run GET request for the object with ID {new_object_id}'):
        get_response = requests.get(f'{api_url}/{new_object_id}')
    with allure.step('Check that response status code is 200'):
        assert get_response.status_code == 200, \
            f'Returned status code {get_response.status_code} while expected 200'
    with allure.step(f'Check that returned object ID is {new_object_id}'):
        assert get_response.json()['id'] == new_object_id, \
            f'Returned object ID {get_response.json()["id"]} while expected {new_object_id}'
    with allure.step(f'Check that returned object name is {create_body["data"]["name"]}'):
        assert get_response.json()['data']['name'] == create_body['data']['name'], \
            f'Returned name {get_response.json()["data"]["name"]} while expected {create_body["data"]["name"]}'


@allure.suite('Objects API')
@allure.feature('Manipulate objects')
@allure.story('Create new object')
@allure.title('Create with correct data')
@allure.severity('Critical')
@pytest.mark.parametrize('iteration', range(3))
@pytest.mark.critical
def test_add_new_object(create_object, iteration):
    create_body, create_response = create_object
    with allure.step('Check that response status code is 200'):
        assert create_response.status_code == 200, \
            f'Returned status code {create_response.status_code} while expected 200'
    with allure.step(f'Check that returned object city is {create_body["name"]}'):
        assert create_response.json()['name'] == create_body['name'], \
            f'Returned city name {create_response.json()["name"]} while expected {create_body["name"]}'
    with allure.step(f'Check that returned object name is {create_body["name"]}'):
        assert create_response.json()['data']['name'] == create_body['data']['name'], \
            f'Returned name {create_response.json()["data"]["name"]} while expected {create_body["data"]["name"]}'


@allure.suite('Objects API')
@allure.feature('Manipulate objects')
@allure.story('Object full update')
@allure.title('Update with correct data')
@allure.severity('Major')
@allure.link('https://reqtest.com/wp-content/uploads/2012/09/38_test_case_template.png')
@allure.issue('https://www.shutterstock.com/image-vector/cartoon-insect-happy-bug-cute-600nw-2508704967.jpg',
              'B-00309')
def test_put_update_object(create_object, api_url):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    with allure.step(f'Run PUT request for the object with ID {new_object_id}'):
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
    with allure.step('Check that response status code is 200'):
        assert put_response.status_code == 200, \
            f'Returned status code {put_response.status_code} while expected 200'
    with allure.step(f'Check that returned object ID is {new_object_id}'):
        assert str(put_response.json()['id']) == str(new_object_id), \
            f'Returned object ID {put_response.json()["id"]} while expected {new_object_id})'
    with allure.step('Check that returned object address is Old Mexico'):
        assert put_response.json()['name'] == 'Old Mexico', \
            f'Returned address {put_response.json()["data"]["address"]} while expected Old Mexico'
    with allure.step('Check that returned data object is not changed'):
        assert put_response.json()['data'] == create_body['data'], \
            f'Returned data object {put_response.json()["data"]} while expected {create_body["data"]}'


@allure.suite('Objects API')
@allure.feature('Manipulate objects')
@allure.story('Object partly update')
@allure.title('Update with correct data')
@allure.severity('Minor')
@pytest.mark.parametrize('name', ['Old York', 'Eldorado', 'Mushmore'])
def test_patch_update_object(create_object, name, api_url):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    with allure.step(f'Run PATCH request for the object with ID {new_object_id}'):
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
    with allure.step('Check that response status code is 200'):
        assert patch_response.status_code == 200, \
            f'Returned status code {patch_response.status_code} while expected 200'
    with allure.step(f'Check that returned object ID is {new_object_id}'):
        assert str(patch_response.json()['id']) == str(new_object_id), \
            f'Returned object ID {patch_response.json()["id"]} while expected {new_object_id})'
    with allure.step(f'Check that returned object name is {name}'):
        assert patch_response.json()['name'] == name, \
            f'Returned name {patch_response.json()["name"]} while expected {name}'
    with allure.step('Check that returned data object contains of 6 elements'):
        assert len(patch_response.json()['data']) == 6, \
            f'Returned {len(patch_response.json()["data"])} elements in "data" object while expected 6'
    with allure.step(f'Check that returned object mail is {create_body["data"]["mail"]}'):
        assert patch_response.json()['data']['mail'] == create_body['data']['mail'], \
            f'Returned mail {patch_response.json()["data"]["mail"]} while expected {create_body["data"]["mail"]}'


@allure.suite('Objects API')
@allure.feature('Manipulate objects')
@allure.story('Delete object by ID')
@allure.title('Delete by existing ID')
@allure.severity('Minor')
def test_delete_object(create_object, api_url):
    create_body, create_response = create_object
    new_object_id = create_response.json()['id']
    url = f'{api_url}/{new_object_id}'
    with allure.step(f'Run DELETE request for the object with ID {new_object_id}'):
        delete_response = requests.delete(url)
        get_object_by_id = requests.get(url)
    with allure.step('Check that response status code is 200'):
        assert delete_response.status_code == 200, \
            f'Returned status code {delete_response.status_code} while expected 200'
    with allure.step('Check that response text is correct'):
        assert delete_response.text == f'Object with id {str(new_object_id)} successfully deleted', \
            f'Returned id {delete_response.text.split()[3]} while expected {new_object_id}'
    with allure.step(f'Check that the object with ID {new_object_id} is not exist'):
        assert get_object_by_id.status_code == 404, \
            f'Returned status coe {get_object_by_id.status_code} while expected 404'
