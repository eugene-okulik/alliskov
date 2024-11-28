from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.demoblaze.com/index.html'


def test_check_added_goods_in_cart(driver, wait):
    driver.implicitly_wait(5)
    driver.get(url)
    actions = ActionChains(driver)
    alert = Alert(driver)
    item_name_on_goods_page = driver.find_element(By.XPATH, '//h4/a[@href="prod.html?idp_=7"]').text
    item_price_on_goods_page = (
        driver.find_element(By.XPATH, '//a[@href="prod.html?idp_=7"]/../../h5').text.split()[0].lstrip('$'))
    actions.move_to_element(driver.find_element(By.XPATH, '//h4/a[@href="prod.html?idp_=7"]'))
    actions.key_down(Keys.CONTROL)
    actions.click(driver.find_element(By.XPATH, '//h4/a[@href="prod.html?idp_=7"]'))
    actions.key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    item_name_at_item_page = driver.find_element(By.XPATH, '//div[@id="tbodyid"]/h2[@class="name"]').text
    item_price_at_item_page = (
        driver.find_element(By.XPATH, '//div[@id="tbodyid"]/h3[@class="price-container"]').text.split()[0].lstrip('$'))
    driver.find_element(By.XPATH, '//a[(@onclick="addToCart(7)") and (text()="Add to cart")]').click()
    wait.until(EC.alert_is_present())
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.XPATH, '//a[@id="cartur"]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody[@id="tbodyid"]/tr/td[2]')))
    item_name_on_cart_page = driver.find_element(By.XPATH, '//tbody[@id="tbodyid"]/tr/td[2]').text
    item_price_on_cart_page = driver.find_element(By.XPATH, '//tbody[@id="tbodyid"]/tr/td[3]').text
    assert item_name_on_goods_page == item_name_at_item_page == item_name_on_cart_page, \
        f'Failed comparing {item_name_on_goods_page} with {item_name_at_item_page} and {item_name_on_cart_page}'
    assert item_price_on_goods_page == item_price_at_item_page == item_price_on_cart_page, \
        f'Failed comparing {item_price_on_goods_page} with {item_price_at_item_page} and {item_price_on_cart_page}'
