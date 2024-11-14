import allure
import requests
from endpoints.endpoint import Endpoint


class FullObjectUpdate(Endpoint):

    def full_object_update(self, object, payload, headers=None):
        headers = headers if headers else self.headers
        self.payload = payload
        self.object_before_update = object
        self.object_id_before_update = object.json()["id"]
        try:
            self.response = requests.put(
                url=f'{self.url}/{self.object_id_before_update}',
                json=payload,
                headers=headers
            )
            self.object_id = self.response.json()['id']
            print(f'\n Test object {self.object_id} updated')
        except requests.exceptions.JSONDecodeError:
            self.object_id = None
            print(f'\n Test object update failed')
        finally:
            self.status_code = self.response.status_code

    @allure.step('Check that ID is not changed')
    def check_id_not_changed(self):
        assert self.object_id == self.object_id_before_update, \
            (f'Returned ID {self.object_id} {type(self.object_id)}'
             f' while expected {self.object_id_before_update} {type(self.object_id_before_update)}')

    @allure.step('Compare payload and response data')
    def check_response_data(self):
        assert self.response.json()['data'] == self.payload['data'], \
            f'Returned object {self.response.json()["data"]} while expected {self.payload["data"]}'

    @allure.step('Check object data after update failed')
    def check_after_update_failed(self):
        assert self.object_before_update.json() == requests.get(f'{self.url}/{self.object_id_before_update}').json(), \
            (f'Returned object data {requests.get(f"{self.url}/{self.object_id_before_update}").json()} '
             f'while expected {self.object_before_update.json()}')
