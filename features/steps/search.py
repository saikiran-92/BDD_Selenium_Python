from behave import *
from features.pages.Home_Page import HomePage
from features.pages.Search_Page import SearchPage


@given(u'I got navigated to home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    expected_title = "Your Store"
    assert context.home_page.verify_title(expected_title)
    print(expected_title)


@when(u'I enter valid product into search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box("HP")


@when(u'I click on search button')
def step_impl(context):
    context.home_page.click_on_search_button()
    context.search_page = SearchPage(context.driver)


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    expected_text = "HP LP3065"
    assert expected_text in context.search_page.display_status_of_prod()


@when(u'I enter Invalid product in search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box("Honda")


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    expected_warn_msg = "There is no product that matches the search criteria."
    assert expected_warn_msg in context.search_page.warning_message_of_invalid_prod()


@when(u'I dont enter any product in search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box("")