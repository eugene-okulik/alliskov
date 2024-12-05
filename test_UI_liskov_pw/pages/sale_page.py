from playwright.sync_api import expect
from test_UI_liskov_pw.pages.locators import sale_page_locators as locators
from test_UI_liskov_pw.pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'
    tab = locators.sale_tab_on_panel

    def check_deal_categories_visibility(self):
        women = self.find(locators.women_deals_category)
        men = self.find(locators.men_deals_category)
        gear = self.find(locators.gear_deals_category)
        expect(women).to_be_visible()
        expect(men).to_be_visible()
        expect(gear).to_be_visible()

    def check_main_promo_link_is(self, reference_link):
        current_link = self.find(locators.main_promo)
        expect(current_link).to_have_attribute('href', reference_link)
