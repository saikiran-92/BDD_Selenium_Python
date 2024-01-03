from selenium.webdriver.common.by import By


class Login_Page:

    def __init__(self, driver):
        self.driver = driver

    email_address_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_text):
        self.driver.find_element(By.XPATH, self.email_address_xpath).send_keys(email_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password_text)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def warning_message(self, expected_warning_message):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text.__contains__(expected_warning_message)

