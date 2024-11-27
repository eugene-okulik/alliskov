import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait
