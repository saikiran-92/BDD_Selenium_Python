class Register_Page:

    def __init__(self,driver):
        self.driver = driver

    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    cpassword_id = "input-confirm"
    click_agree_checkbox = "agree"
    click_register_xpath = "//input[@type='submit']"
    success_message_xpath = "//div[@id='content']/h1"
    warning_message_xpath = "//div[@id='account-register']/div[1]"
