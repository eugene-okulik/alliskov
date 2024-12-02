import re
from playwright.sync_api import Page, expect


def test_authentication_form_login(page: Page):
    url = 'https://the-internet.herokuapp.com'
    page.goto(url)
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('tomsmith')
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')
    page.get_by_role('button', name=re.compile('Login')).click()
    expect(page).to_have_url(f'{url}/secure')
