
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_DOM_include_button_addbusket(browser):
    wait = WebDriverWait(browser, 10)
    add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-add-to-basket'))) #проверка что кнопка в коризину есть
    assert add_button is not None, 'Кнопка существует' #проверям, что текущий язык браузера совпадает с тем что ввел пользователь