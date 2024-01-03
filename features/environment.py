from Webdriver import webdriver


def before_scenario(context, scenario):
    print("Chrome driver executed")
    context.driver = webdriver.get_chrome_webdriver()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")


def after_scenario(context, scenario):
    context.driver.close()
