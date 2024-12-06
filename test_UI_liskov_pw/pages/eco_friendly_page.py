import re
from test_UI_liskov_pw.pages.locators import eco_friendly_page_locators as locators
from test_UI_liskov_pw.pages.base_page import BasePage
from playwright.sync_api import expect
from typing import Literal


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def switch_view_mode_to_list(self):
        self.find(locators.list_mode_switch).click()

    def switch_view_mode_to_grid(self):
        self.find(locators.grid_mode_switch).click()

    def check_active_view_mode_is(self, arg: Literal['grid', 'list']):
        if arg.lower() == 'grid':
            expect(self.find(locators.grid_mode_switch)).to_have_class(re.compile('active'))
        elif arg.lower() == 'list':
            expect(self.find(locators.list_mode_switch)).to_have_class(re.compile('active'))
        else:
            raise NotImplementedError('Entered nonexistent mode name')

    def check_active_sort_type_is_by(self, arg: Literal['name', 'price', 'position']):
        if arg.lower() == 'name':
            expect(self.find(locators.sort_by_name)).to_have_attribute('selected', 'selected')
        elif arg.lower() == 'position':
            expect(self.find(locators.sort_by_position)).to_have_attribute('selected', 'selected')
        elif arg.lower() == 'price':
            expect(self.find(locators.sort_by_price)).to_have_attribute('selected', 'selected')
        else:
            raise NotImplementedError('Entered nonexistent sort type')

    def check_active_sort_direction_is(self, arg: Literal['ascendant', 'descendant']):
        if arg.lower() == 'asc':
            expect(self.find(locators.sort_direction_selector)).to_have_class(re.compile('sort-asc'))
        if arg.lower() == 'desc':
            expect(self.find(locators.sort_direction_selector)).to_have_class(re.compile('sort-desc'))
