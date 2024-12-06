import re
from playwright.sync_api import Page, expect
from test_UI_liskov_pw.pages.locators import base_page_locators as locators


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    tab = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page url was not specified')

    def find(self, locator):
        return self.page.locator(locator)

    def check_tab_title_is(self, title):
        expect(self.page).to_have_title(title)

    def check_page_headline_is(self, headline):
        expect(self.find(locators.headline_locator)).to_have_text(headline)

    def check_search_field_placeholder_text_is(self, reference_text):
        current_text = self.find(locators.search_field)
        (expect(current_text).to_have_attribute('placeholder', reference_text))

    def check_search_field_max_number_of_symbols_is(self, reference_number):
        current_number = self.find(locators.search_field).get_attribute('maxlength')
        expect(current_number).to_have_text(reference_number)

    def fill_search_field_with_value(self, value):
        self.find(locators.search_field).fill(value)

    def check_search_button_is_disabled(self):
        expect(self.find(locators.search_button)).to_be_disabled()

    def check_search_button_is_enabled(self):
        expect(self.find(locators.search_button)).not_to_be_disabled()

    def check_tab_marked_as_active(self):
        expect(self.find(self.tab)).to_have_class(re.compile('active'))
