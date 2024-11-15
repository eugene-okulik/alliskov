import allure
import pytest


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    headers = {'Content-Type': 'application/json'}
    response = None
    status_code = None

    @allure.step('Check that response status code is 200')
    def check_status_200(self):
        assert self.response.status_code == 200, (
            pytest.fail(f'Returned status code {self.response.status_code} while expected 200')
        )

    @allure.step('Check that response status code is 201')
    def check_status_201(self):
        assert self.response.status_code == 201, (
            pytest.fail(f'Returned status code {self.response.status_code} while expected 201')
        )

    @allure.step('Check that response status code is 400')
    def check_status_400(self):
        assert self.response.status_code == 400, (
            pytest.fail(f'Returned status code {self.response.status_code} while expected 400')
        )
