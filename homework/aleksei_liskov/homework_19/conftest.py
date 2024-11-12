import pytest
import requests
import random
from faker import Faker
import allure


@pytest.fixture()
def api_url():
    return 'http://167.172.172.115:52353/object'


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
def count_objects(api_url):
    response = requests.get(api_url)
    objects_quantity = len(response.json()['data'])
    return objects_quantity


@allure.label('Create object')
@pytest.fixture()
def create_object(api_url):
    with allure.step('Create test object'):
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
    with allure.step('Delete test object'):
        requests.delete(f'{api_url}/{object_id}')
