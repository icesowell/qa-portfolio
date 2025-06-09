import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser): #Регистрирует новую опцию в pytest 
    parser.addoption('--language', action='store', default=None, #Сохраняет переданное значение action="store"
                     help="Set browser language for tests: en, ru, fr, etc.")


@pytest.fixture
def browser(request):

    language = request.config.getoption('language') #получаем значение языка из cmd

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language}) #тут мы говорим браузеру какой язык поставить в переменной lang записанной из cmd
    browser = webdriver.Chrome(options=options)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)

    yield browser
    print('\nquet browser...')
    browser.quit()




