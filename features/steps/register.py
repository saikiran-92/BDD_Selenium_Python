from behave import *
from selenium.webdriver.common.by import By
import time
from features.pages.Home_Page import HomePage


@given(u'I navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.click_on_register()


@when(u'I enter mandatory fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("Saikiran100")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Sri22100")
    context.driver.find_element(By.ID, "input-email").send_keys("Saikiran100@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("9123456100")
    context.driver.find_element(By.ID, "input-password").send_keys("Saikiran100")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Saikiran100")


@when(u'I Select Privacy Policy')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.NAME, "agree").click()


@when(u'I click on Register button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then(u'Account should be created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert expected_text in context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text


@when(u'I enter all fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("Saikiran100")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Srii100")
    context.driver.find_element(By.ID, "input-email").send_keys("Saikiran100@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("9123456100")
    context.driver.find_element(By.ID, "input-password").send_keys("Saikiran100")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Saikiran100")
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
    time.sleep(5)


@when(u'I enter all fields except email field')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("Ssaikirannn3222")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Sriiii")
    context.driver.find_element(By.ID, "input-telephone").send_keys("9123412345")
    context.driver.find_element(By.ID, "input-password").send_keys("Saikiran12")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Saikiran12")


@when(u'I enter existing email address on email field')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-email").send_keys("SaikiranSri32@gmail.com")


@then(u'I should get proper warning message')
def step_impl(context):
    expected_warning_msg = "Warning: E-Mail Address is already registered!"
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
            .text.__contains__(expected_warning_msg))
    time.sleep(2)


@when(u'I dont enter anything into fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_imp(context):
    expected_privacy_policy = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"

    assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
            .text.__contains__(expected_privacy_policy))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
            .text.__contains__(expected_first_name_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
            .text.__contains__(expected_last_name_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div")
            .text.__contains__(expected_email_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
            .text.__contains__(expected_telephone_warning))
    assert (context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div")
            .text.__contains__(expected_password_warning))


@then(u'I should get Proper warning message every mandatory fields should be displayed')
def step_impl(context):
    expected_warning_msg_empty_fields = "Warning: You must agree to the Privacy Policy!"
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
            .text.__contains__(expected_warning_msg_empty_fields))
    time.sleep(2)


@when(u'I click on Policy check box')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.NAME, "agree").click()


@then(u'I should get Proper warning message are you an existing user')
def step_impl(context):
    expected_warning_msg_empty_fields_with_policy = "If you already have an account with us, please login at the login page."
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
            .text.__contains__(expected_warning_msg_empty_fields_with_policy))
    time.sleep(2)
