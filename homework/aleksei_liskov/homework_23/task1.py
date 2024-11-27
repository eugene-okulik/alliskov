from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

url = 'https://www.qa-practice.com/elements/input/simple'
driver.get(url)
text_field = driver.find_element(By.XPATH, '//input[@placeholder="Submit me"]')
text_field.send_keys('SomeText')
text_field.submit()
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="result"]')))
result = driver.find_element(By.XPATH, '//div[@id="result"]')
print(result.text)
