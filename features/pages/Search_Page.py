from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self,driver):
        self.driver = driver

    valid_prod_link_text = "//a[text()='HP LP3065']"
    warning_message_of_invalid_product_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_prod(self):
        return self.driver.find_element(By.XPATH, self.valid_prod_link_text).text

    def warning_message_of_invalid_prod(self):
        return self.driver.find_element(By.XPATH, self.warning_message_of_invalid_product_xpath).text