from selenium import webdriver


def get_chrome_webdriver():
    driver = webdriver.Chrome()
    return driver