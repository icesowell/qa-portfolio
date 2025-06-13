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

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_TEXT_BUSKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_TITILE = (By.XPATH, '//h1')
    PRICE_TITLE = (By.CSS_SELECTOR, '.product_main .price_color')
    BUSKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')