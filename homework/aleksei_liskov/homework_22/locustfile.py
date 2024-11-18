from locust import task, HttpUser, tag
import requests
import random
from faker import Faker


class DummyJsonUser(HttpUser):
    fake = None
    user_id = None
    user_name = None
    password = None
    token = None

    def on_start(self):
        self.fake = Faker()
        get_users_response = requests.get('https://dummyjson.com/users')
        users_count = len(get_users_response.json()['users'])
        self.user_id = random.randrange(start=0, stop=users_count)
        self.user_name = get_users_response.json()['users'][self.user_id]['username']
        self.password = get_users_response.json()['users'][self.user_id]['password']
        authorization_response = requests.post(
            url='https://dummyjson.com/auth/login',
            json={"username": self.user_name, "password": self.password}
        )
        self.token = authorization_response.json()['accessToken']

    @tag('critical')
    @task(2)
    def get_all_users(self):
        self.client.get('/users')

    @tag('normal')
    @task(3)
    def get_one_user(self):
        self.client.get(f'/users/{self.user_id}')

    @tag('critical')
    @task(1)
    def user_login(self):
        self.client.post(url='/auth/login', json={'username': self.user_name, 'password': self.password})

    @tag('normal')
    @task(1)
    def check_authorization(self):
        self.client.get(url='/auth/me', headers={'Authorization': f'Bearer {self.token}'})

    @tag('normal')
    @task(1)
    def update_user(self):
        self.client.patch(url=f'/users/{self.user_id}',
                          json={'lastName': self.fake.last_name()})

    @tag('minor')
    @task(1)
    def delete_user(self):
        self.client.delete(url=f'/users/{self.user_id}')
