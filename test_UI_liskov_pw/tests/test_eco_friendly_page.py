import allure


@allure.suite('Magento Web')
@allure.feature('Eco Friendly Page')
@allure.story('Positive')
@allure.title('Eco Friendly page has correct title')
@allure.severity('Minor')
def test_sale_page_title(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_tab_title_is('Eco Friendly')


@allure.suite('Magento Web')
@allure.feature('Eco Friendly Page')
@allure.story('Positive')
@allure.title('Eco Friendly page has correct headline')
@allure.severity('Major')
def test_sale_page_headline(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_page_headline_is('Eco Friendly')


@allure.suite('Magento Web')
@allure.feature('Eco Friendly Page')
@allure.story('Positive')
@allure.title('Eco Friendly items list has default sort by position')
@allure.severity('Minor')
def test_default_sort_type_is_by_position(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_active_sort_type_is_by('position')


@allure.suite('Magento Web')
@allure.feature('Eco Friendly Page')
@allure.story('Positive')
@allure.title('Eco Friendly items list has default ascendant sort direction')
@allure.severity('Minor')
def test_default_sort_direction_is_ascendant(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_active_sort_direction_is('ascendant')


@allure.suite('Magento Web')
@allure.feature('Eco Friendly Page')
@allure.story('Positive')
@allure.title('Switch Eco Friendly items view mode from list to grid')
@allure.severity('Minor')
def test_switch_view_mode_to_list(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_active_view_mode_is('grid')
    eco_friendly_page.switch_view_mode_to_list()
    eco_friendly_page.check_active_view_mode_is('list')


@allure.suite('Magento Web')
@allure.feature('Eco Friendly Page')
@allure.story('Positive')
@allure.title('Search button enables if search field is not empty')
@allure.severity('Minor')
def test_search_button_enabled_if_input_is_not_empty(eco_friendly_page, random_value):
    eco_friendly_page.open_page()
    eco_friendly_page.check_search_button_is_disabled()
    eco_friendly_page.fill_search_field_with_value(random_value)
    eco_friendly_page.check_search_button_is_enabled()
