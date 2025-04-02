from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
    
    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def enter_credentials(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_logged_in(self):
        return self.page.locator("div.flash.success").is_visible()
