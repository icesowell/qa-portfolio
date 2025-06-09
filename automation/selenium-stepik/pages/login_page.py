from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_BTN = (By.CSS_SELECTOR, "a.navbar__auth_login")  # Надёжный селектор
    EMAIL_INPUT = (By.ID, 'id_login_email')
    PASSWORD_INPUT = (By.ID, 'id_login_password')
    SUBMIT_BTN = (By.CSS_SELECTOR, "[type='submit']")

    def login(self, email, password):
        self.click(self.LOGIN_BTN)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BTN)
