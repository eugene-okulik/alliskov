first_name_input = '//input[@id="firstname"]'
last_name_input = '//input[@id="lastname"]'
email_input = '//input[@id="email_address"]'
password_input = '//input[@id="password"]'
password_confirmation_input = '//input[@id="password-confirmation"]'
password_strength_meter_container = '//div[@id="password-strength-meter-container"]'
password_strength_meter = '//div[@id="password-strength-meter"]//span'
create_button = \
    '//button[(@type="submit") and (@title="Create an Account")]'
first_name_requirement_warning = \
    '//div[(@for="firstname") and (text()="This is a required field.")]'
last_name_requirement_warning = \
    '//div[(@for="lastname") and (text()="This is a required field.")]'
email_requirement_warning = \
    '//div[(@for="email_address") and (text()="This is a required field.")]'
password_requirement_warning = \
    '//div[(@for="password") and (text()="This is a required field.")]'
password_confirmation_requirement_warning = \
    '//div[(@for="password-confirmation") and (text()="This is a required field.")]'
