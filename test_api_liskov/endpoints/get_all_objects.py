import requests
import allure
from endpoints.endpoint import Endpoint


class GetAllObjects(Endpoint):

    @allure.step('Receive all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        return self.response

    @allure.step('Check that quantity of the received objects is correct')
    def compare_objects_quantity_before_and_after(self, quantity_before, creation_status_code):
        if creation_status_code in [200, 201]:
            assert len(self.response.json()['data']) == quantity_before + 1, \
                f'Returned objects number {len(self.response.json()["data"])} while expected {quantity_before + 1}'
        else:
            assert len(self.response.json()['data']) == quantity_before, \
                f'Returned objects number {len(self.response.json()["data"])} while expected {quantity_before}'
