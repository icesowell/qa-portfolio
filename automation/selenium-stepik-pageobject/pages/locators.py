from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    REGISTATION_LINK = (By.ID, "registration_link")

class LoginPageLocators():

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name = 'registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "[name = 'registration-password2']")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name = 'login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name = 'login-password']")