import allure
import requests
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.payload = payload
        try:
            self.response = requests.post(
                url=self.url,
                json=payload,
                headers=headers
            )
            print(f'\n Test object created with ID {self.response.json()["id"]}')
        except requests.exceptions.JSONDecodeError:
            self.object_id = None
            print(f'\n Test object creation failed')
        finally:
            self.status_code = self.response.status_code

    @allure.step('Check that ID assigned to the object')
    def check_id(self):
        assert self.response.json()["id"], f'ID has not returned'

    @allure.step('Compare payload and response data')
    def check_response_data(self):
        assert self.response.json()['data'] == self.payload['data'], \
            f'Returned object {self.response.json()["data"]} while expected {self.payload["data"]}'
