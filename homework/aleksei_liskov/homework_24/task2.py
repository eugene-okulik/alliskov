from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://magento.softwaretestingboard.com/gear/bags.html'


def test_check_added_product_displayed_at_compare_tab(driver):
    driver.implicitly_wait(5)
    driver.get(url)
    actions = ActionChains(driver)
    first_item_xpath = '//ol[contains(@class, "products")]/li[1]'
    first_item_name = driver.find_element(
        By.XPATH, f'{first_item_xpath}//a[@class="product-item-link"]').text
    first_item_id = driver.find_element(
        By.XPATH, f'{first_item_xpath}//div[@data-role="priceBox"]').get_attribute('data-product-id')
    driver.execute_script('arguments[0].scrollIntoView()', driver.find_element(By.XPATH, first_item_xpath))
    actions.move_to_element(driver.find_element(By.XPATH, f'{first_item_xpath}'))
    actions.click(driver.find_element(By.XPATH, f'{first_item_xpath}//a[@title="Add to Compare"]'))
    actions.perform()
    item_at_compare_tab_xpath = '//ol[@id="compare-items"]/li[1]'
    item_at_compare_tab_name = driver.find_element(By.XPATH, f'{item_at_compare_tab_xpath}/strong/a').text
    item_at_compare_tab_id = driver.find_element(By.XPATH, f'{item_at_compare_tab_xpath}/input').get_attribute('value')
    assert first_item_id == item_at_compare_tab_id, \
        f'Failed comparing {first_item_id} with {item_at_compare_tab_id}'
    assert first_item_name == item_at_compare_tab_name, \
        f'Failed comparing {first_item_name} with {item_at_compare_tab_name}'
