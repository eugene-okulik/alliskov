import pytest
import allure


@allure.suite('Magento Web')
@allure.feature('Create Customer Account Page')
@allure.story('Positive')
@allure.title('Account creation page has correct title')
@allure.severity('Minor')
def test_create_page_title(create_account_page):
    create_account_page.open_page()
    create_account_page.check_tab_title_is('Create New Customer Account')


@allure.suite('Magento Web')
@allure.feature('Create Customer Account Page')
@allure.story('Positive')
@allure.title('Account creation page has headline title')
@allure.severity('Major')
def test_create_page_headline(create_account_page):
    create_account_page.open_page()
    create_account_page.check_page_headline_is('Create New Customer Account')


@allure.suite('Magento Web')
@allure.feature('Create Customer Account Page')
@allure.story('Positive')
@allure.title('Account creation with valid data')
@allure.severity('Critical')
def test_create_account_with_valid_data(create_account_page):
    create_account_page.open_page()
    create_account_page.check_tab_title_is('Create New Customer Account')
    create_account_page.fulfill_registration_form()
    create_account_page.click_create_button()
    create_account_page.check_tab_title_is('My Account')


@allure.suite('Magento Web')
@allure.feature('Create Customer Account Page')
@allure.story('Negative')
@allure.title('Account creation with empty field')
@allure.severity('Major')
@pytest.mark.parametrize('field', ['first_name', 'last_name', 'email', 'password', 'password_confirmation'])
def test_create_account_with_empty_field(create_account_page, field):
    create_account_page.open_page()
    create_account_page.fill_registration_form_with_empty_field(field)
    create_account_page.click_create_button()
    create_account_page.check_warning_message_under_field(field)


@allure.suite('Magento Web')
@allure.feature('Create Customer Account Page')
@allure.story('Positive')
@allure.title('Password strength meter correctly defines password complexity')
@allure.severity('Major')
@pytest.mark.parametrize('password, text', [('empty', 'No Password'), ('1', 'Weak'), ('123456qwE!', 'Medium'),
                                            ('123456qwE!@#', 'Strong'), ('123456qwE!QWE@#$', 'Very Strong')])
def test_password_strength_meter_text(create_account_page, password, text):
    create_account_page.open_page()
    create_account_page.fulfill_registration_form(password=password)
    create_account_page.check_password_strength_meter_text(text=text)
