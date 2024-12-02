from datetime import datetime
from playwright.sync_api import Page, expect


def convert_date(date: str):
    income_date = datetime.strptime(date, '%m.%d.%Y')
    outcome_date = income_date.strftime('%d %B,%Y')
    return outcome_date


def test_student_registration(page: Page):
    url = 'https://demoqa.com/automation-practice-form'
    page.goto(url)
    page.get_by_placeholder('First Name').fill('John')
    page.get_by_role('textbox', name='last Name').fill('Doe')
    page.get_by_placeholder('name@example.com').fill('johnnydoey@test.com')
    page.locator('//label[@for="gender-radio-1"]').click()
    page.locator('//input[@id="userNumber"]').fill('1234567890')
    page.locator('input#dateOfBirthInput').press('Control+a')
    page.locator('input#dateOfBirthInput').fill('02.12.2000')
    page.keyboard.press('Tab')
    page.locator('//input[@id="subjectsInput"]').press_sequentially('arts', delay=100)
    page.keyboard.press('Tab')
    page.locator('//label[(@for="hobbies-checkbox-1") and (text()="Sports")]').click()
    page.get_by_placeholder('Current Address').fill('Country 1, City 2, Street 3, Housebuilding 4, Apartment 5')
    page.focus('//div[text()="Select State"]/..//input')
    page.locator('//div[text()="Select State"]/..//input').press_sequentially('NCR', delay=100)
    page.keyboard.press('Enter')
    page.locator('//div[text()="Select City"]/..//input').press_sequentially('Delhi', delay=100)
    page.keyboard.press('Enter')
    page.locator('//button[@id="submit"]').click()

    expect(page.locator
           (f'//tbody//td[text()="Student Name"]/following-sibling::td[1]')).to_have_text('John Doe')
    expect(page.locator
           (f'//tbody//td[text()="Student Email"]/following-sibling::td[1]')).to_have_text('johnnydoey@test.com')
    expect(page.locator
           (f'//tbody//td[text()="Gender"]/following-sibling::td[1]')).to_have_text('Male')
    expect(page.locator
           (f'//tbody//td[text()="Mobile"]/following-sibling::td[1]')).to_have_text('1234567890')
    expect(page.locator
           (f'//tbody//td[text()="Date of Birth"]/following-sibling::td[1]')).to_have_text(convert_date('02.12.2000'))
    expect(page.locator
           (f'//tbody//td[text()="Subjects"]/following-sibling::td[1]')).to_have_text('Arts')
    expect(page.locator
           (f'//tbody//td[text()="Hobbies"]/following-sibling::td[1]')).to_have_text('Sports')
    expect(page.locator
           (f'//tbody//td[text()="Address"]/following-sibling::td[1]')
           ).to_have_text('Country 1, City 2, Street 3, Housebuilding 4, Apartment 5')
    expect(page.locator
           (f'//tbody//td[text()="State and City"]/following-sibling::td[1]')).to_have_text('NCR Delhi')
