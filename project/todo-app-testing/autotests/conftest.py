"""
Fixture
"""
import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os


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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания отчёта и добавления скриншота в случае ошибки.
    """
    outcome = yield
    rep = outcome.get_result()

    # Проверяем, что тест упал и у него есть доступ к фикстуре browser
    if rep.when == "call" and rep.failed:
        browser = item.funcargs.get("browser")
        if browser:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
            browser.save_screenshot(screenshot_path)

            # Прикрепляем скриншот к Allure-отчёту
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name=f"{item.name}_screenshot", attachment_type=allure.attachment_type.PNG)
