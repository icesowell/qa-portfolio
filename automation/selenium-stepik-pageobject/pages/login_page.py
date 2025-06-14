from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL) 
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)

    def register_new_user(self, email, password):
        email_imput = self.wait_for_element(LoginPageLocators.REGISTRATION_EMAIL)
        password_input = self.wait_for_element(LoginPageLocators.REGISTRATION_PASSWORD)
        password_confirm_input = self.wait_for_element(LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        confirm_button = self.wait_for_element(LoginPageLocators.REGISTRATION_CONFIRM_BUTTON)

        email_imput.send_keys(email)
        password_input.send_keys(password)
        password_confirm_input.send_keys(password)
        confirm_button.click()
        