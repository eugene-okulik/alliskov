import allure


@allure.suite('Magento Web')
@allure.feature('Sale Page')
@allure.story('Positive')
@allure.title('Sale page has correct title')
@allure.severity('Minor')
def test_sale_page_title(sale_page):
    sale_page.open_page()
    sale_page.check_tab_title_is('Sale')


@allure.suite('Magento Web')
@allure.feature('Sale Page')
@allure.story('Positive')
@allure.title('Sale page has correct headline')
@allure.severity('Major')
def test_sale_page_headline(sale_page):
    sale_page.open_page()
    sale_page.check_page_headline_is('Sale')


@allure.suite('Magento Web')
@allure.feature('Sale Page')
@allure.story('Positive')
@allure.title('Sale page marked as active on the tab panel')
@allure.severity('Minor')
def test_sale_tab_is_marked_as_active_on_tab_panel(sale_page):
    sale_page.open_page()
    sale_page.check_tab_marked_as_active()


@allure.suite('Magento Web')
@allure.feature('Sale Page')
@allure.story('Positive')
@allure.title('Deals categories are visible on the sale page')
@allure.severity('Critical')
def test_sale_page_deal_categories_are_visible(sale_page):
    sale_page.open_page()
    sale_page.check_deal_categories_visibility()


@allure.suite('Magento Web')
@allure.feature('Sale Page')
@allure.story('Positive')
@allure.title('Main promo banner has correct link')
@allure.severity('Major')
def test_sale_page_main_promo_link(sale_page):
    sale_page.open_page()
    sale_page.check_main_promo_link_is('https://magento.softwaretestingboard.com/promotions/women-sale.html')


@allure.suite('Magento Web')
@allure.feature('Sale Page')
@allure.story('Positive')
@allure.title('Search field has correct placeholder text')
@allure.severity('Minor')
def test_search_field_placeholder_text(sale_page):
    sale_page.open_page()
    sale_page.check_search_field_placeholder_text_is('Search entire store here...')
