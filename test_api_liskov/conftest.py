import pytest
import random
import allure
from faker import Faker
from endpoints.get_all_objects import GetAllObjects
from endpoints.get_one_object import GetOneObject
from endpoints.create_object import CreateObject
from endpoints.put_update_object import FullObjectUpdate
from endpoints.patch_update_object import PartiallyObjectUpdate
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def payload(request):
    custom_payload = getattr(request, 'param', None)
    if not custom_payload:
        payload = {
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
    else:
        payload = custom_payload
    return payload


@pytest.fixture()
def get_all_objects_endpoint():
    return GetAllObjects()


@pytest.fixture()
def get_one_object_endpoint():
    return GetOneObject()


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def full_object_update_endpoint():
    return FullObjectUpdate()


@pytest.fixture()
def partially_object_update_endpoint():
    return PartiallyObjectUpdate()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@allure.step('Prepare test object')
@pytest.fixture()
def new_object(payload, create_object_endpoint, delete_object_endpoint):
    with allure.step('Create object'):
        create_object_endpoint.create_new_object(payload)
        yield create_object_endpoint.response
    with allure.step('Delete object'):
        delete_object_endpoint.delete_object(create_object_endpoint.response)


@pytest.fixture()
def count_objects(get_all_objects_endpoint):
    response_json = get_all_objects_endpoint.get_all_objects().json()
    objects_quantity = len(response_json['data'])
    return objects_quantity
