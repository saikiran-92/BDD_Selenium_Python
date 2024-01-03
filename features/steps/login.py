from behave import *
import time
from datetime import datetime
from features.pages.Account_Page import Account_Page
from features.pages.Home_Page import HomePage
from features.pages.Login_Page import Login_Page


@given(u'I got navigate to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.click_on_login()

    context.login_page = Login_Page(context.driver)


@when(u'I enter valid email id and valid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("saik@gmail.com")
    context.login_page.enter_password("Saikiran")


@when(u'I click on login button')
def step_impl(context):
    context.login_page.click_on_login()


@then(u'I should logged in')
def step_impl(context):
    context.account_page = Account_Page(context.driver)
    expected_text = "Edit your account information"
    assert expected_text in context.account_page.account_info()


@when(u'I enter invalid email id and valid password into the fields')
def step_impl(context):
    time.sleep(3)
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sai" + time_stamp + "@gmail.com"
    context.login_page = Login_Page(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("Saikiran")


@then(u'I should get Proper warning message Invalid Email id')
def step_impl(context):
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.warning_message(expected_warning_msg)


@when(u'I enter valid email id and invalid password into fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_password = "sai" + time_stamp + "12345"
    context.login_page.enter_email_address("saik@gmail.com")
    context.login_page.enter_password(invalid_password)


@then(u'I should get proper warning message Enter Email id and Password')
def step_impl(context):
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.warning_message(expected_warning_msg)


@then(u'I should get proper warning message Invalid Password')
def step_impl(context):
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.warning_message(expected_warning_msg)


@when(u'I not enter email id and password into fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")