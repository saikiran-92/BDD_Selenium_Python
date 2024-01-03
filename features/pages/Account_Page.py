from selenium.webdriver.common.by import By


class Account_Page:

    def __init__(self, driver):
        self.driver = driver

    edit_account_info_link_text = "//a[text()='Edit your account information']"

    def account_info(self):
        return self.driver.find_element(By.XPATH, self.edit_account_info_link_text).text