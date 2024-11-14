import allure
import requests
from endpoints.endpoint import Endpoint


class PartiallyObjectUpdate(Endpoint):

    def partially_object_update(self, object, payload, headers=None):
        headers = headers if headers else self.headers
        self.payload = payload
        self.object_before_update = object
        self.object_id_before_update = object.json()["id"]
        try:
            self.response = requests.patch(
                url=f'{self.url}/{self.object_id_before_update}',
                json=payload,
                headers=headers
            )
            self.object_id = self.response.json()['id']
            print(f'\n Test object {self.object_id} updated')
        except requests.exceptions.JSONDecodeError:
            self.object_id = None
            print('\n Test object update failed')
        finally:
            self.status_code = self.response.status_code

    @allure.step('Check that ID is not changed')
    def check_id_not_changed(self):
        assert self.object_id == self.object_id_before_update, \
            (f'Returned ID {self.object_id} {type(self.object_id)}'
             f' while expected {self.object_id_before_update} {type(self.object_id_before_update)}')

    @allure.step('Check object data after update failed')
    def check_after_update_failed(self):
        assert self.object_before_update.json() == requests.get(f'{self.url}/{self.object_id_before_update}').json(), \
            (f'Returned object data {requests.get(f"{self.url}/{self.object_id_before_update}").json()} '
             f'while expected {self.object_before_update.json()}')

    @allure.step('Check data object is not changed')
    def check_object_data_not_changed(self):
        assert self.response.json()["data"] == self.object_before_update.json()["data"], \
            f'Returned {self.response.json()["data"]} while expected {self.object_before_update.json()["data"]}'

    @allure.step('Check state name changed')
    def check_state_name_changed(self, data):
        assert self.response.json()["name"] == data["name"], \
            f'Returned {self.response.json()["name"]} while expected {data["name"]}'
