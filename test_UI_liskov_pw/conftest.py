import pytest
from faker import Faker
from test_UI_liskov_pw.pages.sale_page import SalePage
from test_UI_liskov_pw.pages.eco_friendly_page import EcoFriendly
from test_UI_liskov_pw.pages.create_account_page import CreateAccount


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()
def create_account_page(page):
    return CreateAccount(page)


@pytest.fixture()
def random_value():
    return ''.join(Faker().random_letters(10))
