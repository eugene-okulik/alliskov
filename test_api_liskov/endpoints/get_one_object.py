import requests
import allure
from endpoints.endpoint import Endpoint


class GetOneObject(Endpoint):
    object_id = None

    @allure.step('Receive one object by ID')
    def get_one_object(self, object):
        self.object_id = object.json()["id"]
        self.response = requests.get(f'{self.url}/{self.object_id}')

    @allure.step('Compare data object at payload and response')
    def compare_object_data(self, object, payload):
        response_data = self.response.json()['data']
        assert response_data == payload["data"], f'Returned object {response_data} while expected {payload["data"]}'

    @allure.step('Check object after deletion')
    def check_object_after_deletion(self, object_id=None):
        object_id = object_id if object_id else self.object_id
        assert requests.get(f'{self.url}/{self.object_id}').status_code == 404
