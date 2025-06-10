from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.ID, 'login_link'), "На сайте нет ссылки на логин"