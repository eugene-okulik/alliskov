import allure
import requests
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object by ID')
    def delete_object(self, object):
        if str(object.status_code) == '200':
            object_id = object.json()['id']
            self.response = requests.delete(f'{self.url}/{object_id}')
            if self.response.status_code == 200:
                print(f'\n Test object ID {object_id} deleted')
            else:
                print(f'\n Test object ID {object_id} delete failed. '
                      f'Response status code is {self.response.status_code}')
        else:
            print('\n Nothing to delete')
