from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
actions = ActionChains(driver)

url = 'https://demoqa.com/automation-practice-form'
driver.get(url)
# find_elements
first_name = driver.find_element(By.XPATH, '//input[@id="firstName"]')
last_name = driver.find_element(By.XPATH, '//input[@id="lastName"]')
email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
gender_male = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
phone_number = driver.find_element(By.XPATH, '//input[@id="userNumber"]')
date_of_birth = driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]')
subjects = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
hobbies_music = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
current_address = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
state = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
city = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
# actions
first_name.send_keys('Peter')
last_name.send_keys('Pan')
email.send_keys('shadow@neverland.com')
gender_male.click()
phone_number.send_keys('0102030405')
date_of_birth.click()
actions.click(date_of_birth).key_down(Keys.CONTROL).send_keys('A') \
    .key_up(Keys.CONTROL).send_keys('11.11.1911').send_keys(Keys.ENTER).perform()
driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", subjects)
subjects.click()
subjects.send_keys('Arts')
subjects.send_keys(Keys.TAB)
hobbies_music.click()
current_address.send_keys('Neverland, The Tree House')
state.send_keys('Haryana')
state.send_keys(Keys.TAB)
city.send_keys('Karnal')
city.send_keys(Keys.TAB)
submit_button = driver.find_element(By.XPATH, '//button[@id="submit"]')
submit_button.click()
rows = driver.find_elements(By.XPATH, '//tbody/tr')
for row in range(1, len(rows)):
    print(driver.find_element(By.XPATH, f'//tbody/tr[{row}]/td[1]').text + ':',
          driver.find_element(By.XPATH, f'//tbody/tr[{row}]/td[2]').text)
