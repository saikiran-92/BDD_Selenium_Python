from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import ConfigReader


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com")
(driver.find_element(By.ID, "input-username")
 .send_keys(ConfigReader.read_configuration("account details", "username")))
(driver.find_element(By.ID, "input-password")
 .send_keys(ConfigReader.read_configuration("account details", "password")))
driver.find_element(By.ID, "submit").click()