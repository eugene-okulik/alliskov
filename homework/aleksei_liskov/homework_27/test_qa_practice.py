from playwright.sync_api import Page, expect, BrowserContext


def test_confirmation_text(page: Page):
    page.on('dialog', lambda dialog: dialog.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')
    page.locator('//a[(@class="a-button") and (text()="Click")]').click()
    result_text = page.locator('//div[@id="result"]/p[@class="result-text"]')
    expect(result_text).to_have_text('Ok')


def test_open_page_in_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.locator('//a[@id="new-page-button"]')
    with context.expect_page() as new_page_event:
        button.click()
    new_page = new_page_event.value
    expect(new_page.locator('//p[@id="result-text"]')).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()
