import json
import urllib.parse
import subprocess
from playwright.sync_api import sync_playwright
from behave import given, when, then
from pages.login_page import LoginPage
import allure

capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",
    "LT:Options": {
        "user": "",
        "accessKey": "",
        "build": "Playwright Allure Integration",
        "name": "Behave Test",
        "platform": "Windows 10",
        "headless": False
    }
}

playwright = sync_playwright().start()

def connect_to_lambda_test():
    playwright_version = str(subprocess.getoutput("playwright --version")).strip().split(" ")[1]
    capabilities["LT:Options"]["playwrightClientVersion"] = playwright_version
    lt_cdp_url = "wss://cdp.lambdatest.com/playwright?capabilities=" + urllib.parse.quote(json.dumps(capabilities))

    print(f"Connecting to: {lt_cdp_url}")

    browser = playwright.chromium.connect(lt_cdp_url, timeout=120000)
    return browser.new_page()

@given("I open the Heroku login page")
def open_login_page(context):
    context.page = connect_to_lambda_test()
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()
    allure.attach(context.page.screenshot(), name="Login Page", attachment_type=allure.attachment_type.PNG)

@when("I enter valid Heroku credentials")
def enter_credentials(context):
    context.login_page.enter_credentials("tomsmith", "SuperSecretPassword!")
    allure.attach(context.page.screenshot(), name="Entered Credentials", attachment_type=allure.attachment_type.PNG)

@then("I should be logged into Heroku successfully")
def verify_login(context):
    assert context.login_page.is_logged_in(), "Login failed!"
    allure.attach(context.page.screenshot(), name="Login Success", attachment_type=allure.attachment_type.PNG)

def after_all(context):
    playwright.stop()
