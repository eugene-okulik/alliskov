import re
from playwright.sync_api import Page, expect


def test_click_button_with_red_text(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')

    # Вариант с expect
    text_color_changing_button = page.locator('//button[@id="colorChange"]')
    expect(text_color_changing_button).to_have_class(re.compile('text-danger'))
    text_color_changing_button.click()

    # Вариант с wait_for_selector
    text_color_changing_button_locator = '//button[(@id="colorChange") and (contains(@class, "text-danger"))]'
    page.wait_for_selector(text_color_changing_button_locator)
    page.locator(text_color_changing_button_locator).click()
