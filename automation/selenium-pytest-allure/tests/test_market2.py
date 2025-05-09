"""
icesowell 2025 (c)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip


MAIN_URL = "https://market.yandex.ru/"

def test_article_search(browser):
    '''
    тест копи артикуля
    '''
    browser.get(MAIN_URL)

    #Нажимаем на первый снипет
    snippet = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.ds-text_lineClamp_2'))
    )
    snippet.click()

    #меняем фокус на открытую вкладку снипета
    tabs = browser.window_handles
    browser.switch_to.window(tabs[-1])

    #нажимаем на кнопку копирования артикуля
    article = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='about-copy']"))
    )
    browser.execute_script("arguments[0].focus();", article)
    article.click()

    #фокус + клик на поисковую строку
    header_search = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#header-search'))
    )
    browser.execute_script("arguments[0].focus();", header_search)
    header_search.click()

    #вставляем из буфера обмена артикул
    act = ActionChains(browser)
    act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    #записываем артикул в переменную
    article_number_1 = pyperclip.paste()

    #фокус + клик на кнопку найти в поиске
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@data-auto='search-button']"))
    )
    browser.execute_script("arguments[0].focus();", button)
    button.click()

    #нажимаем на кнопку копирования артикуля еще раз
    article_2 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='about-copy']"))
    )
    browser.execute_script("arguments[0].focus();", article_2)
    article_2.click()


    #записываем артикул во вторую переменную
    article_number_2 = pyperclip.paste()

    #сверяем что артикулы равны
    assert article_number_1 == article_number_2 , f"Артикулы не равны! article_number_1: {article_number_1}, article_number_2: {article_number_2}"


    #переходим по ссылке со скопированным артикулом
    article_url ='https://market.yandex.ru/product--pliushevoe-kreslo-v-stile-little-petra/pr/' + article_number_2
    browser.get(article_url)
