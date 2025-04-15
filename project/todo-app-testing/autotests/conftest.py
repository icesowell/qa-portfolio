
"""
Fixture
"""
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session") #явно указываем что эта функция это фикстура
def browser():
    """
    Main fixture
    """
    #Оптимизируем запуск браузера
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") #open Browser in maximized mode
    chrome_options.add_argument("--disable-extensions") #disable extensions

    #disable inforbars
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Автоматическая установка и настройка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver #если что то произошло экстренно, то браузер и драйвер принудительно закроется
    driver.quit()
