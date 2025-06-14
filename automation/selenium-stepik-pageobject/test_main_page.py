from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 

    page.open() #open page
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)

    login_page.should_be_login_page()

def test_guest_can_see_login_from(browser):

    login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

    login = LoginPage(browser, login_link)

    login.open()

    login.should_be_login_url()

    login.should_be_login_form()

def test_guest_can_see_register_from(browser):
    register_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

    register = LoginPage(browser, register_link)

    register.open()

    register.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    LINK = 'http://selenium1py.pythonanywhere.com/ru/'

    page = MainPage(browser, LINK)
    page.open()

    page.go_to_busket()

    basket_page = BasketPage(browser, browser.current_url)

    basket_page.should_be_empty_text_basket()
    basket_page.should_be_not_include_items()
    time.sleep(5)