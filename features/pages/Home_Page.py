from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    my_account_xpath = "//span[text()='My Account']"
    login_xpath = "Login"
    register_xpath = "Register"
    search_box_field = "//input[@name='search']"
    search_button_xpath = "//div[@id='search']//button"

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_on_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_xpath).click()

    def click_on_register(self):
        self.driver.find_element(By.LINK_TEXT, self.register_xpath).click()

    def verify_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def enter_product_into_search_box(self, prod_name):
        self.driver.find_element(By.XPATH, self.search_box_field).send_keys(prod_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
