from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def test_choose_language(driver):
    language = 'JavaScript'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    language_select = driver.find_element(By.XPATH, '//select[@name="choose_language"]')
    dropdown = Select(language_select)
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    dropdown.select_by_visible_text(language)
    submit_button.click()
    result_text = driver.find_element(By.XPATH, '//div[@id="result"]/p[@id="result-text"]').text
    assert result_text == language, f'Returned result text {result_text} while expected {language}'


def test_check_text_presence(driver, wait):
    text = 'Hello World!'
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, '//button[text()="Start"]')
    start_button.click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="finish"]')))
    final_text = driver.find_element(By.XPATH, '//div[@id="finish"]').text
    assert final_text == text, f'Returned text {final_text} while expected {text}'
