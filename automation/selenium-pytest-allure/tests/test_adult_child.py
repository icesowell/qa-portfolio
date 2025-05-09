"""
18+ access test
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# URL страницы с товаром 18+
PRODUCT_URL = "https://market.yandex.ru/product--vibrator/921285741?sku=103702452156&uniqueId=182098199&do-waremd5=84f34POlzrWT6wAyROgrIw&sponsored=1&cpc=Oj2WhsNqXzce7D98nwSkOtp7ChzCN8rNIYzFoWldkzg7SrEZkINbQ5DLBfL0j22gV8PhLA4hcfB3VDGZ2z41eAmSaPwuT4zhnL9aRAO4Mbv8hcCP9vE3lbo6d_S_M_o8ZghIg3413el40eV240yXvTchUvB7yq1LLDw7WVAcG1o8BQ9TzVjo5PCQpNvJ4j1EsPB-kJBUCn1rBeCqhQ7vyM_FUgOvPYMGToS-yN7VrWw93bsXaLJhxOysZEBVDTM6jCAxZpz4L1E-qvpglIx13Y6wQ0DtICYJ_Zrz7qwuv-vuQvB-e6dHlGYgOXeVBp8_iu_Ub0F1Sk8N41lVe0FQLMCYZVxRGeAPeoZtKjtiy0tH-oSEgQo3ffVG87Irb_2afeoSoGEqqdT_oarAtaiIqnT7XoUYTzF_KnZti-XlkOT-Qh1KkVaBLuACDWrg_FekUyl15xV2-7SDezA2ZHLiN--bUAZIb1UH62G1dYOsicmxR4knqYoCVQ%2C%2C&nid=54518"
REDIRECT_URL = "https://market.yandex.ru/"

@pytest.mark.parametrize("button_xpath, expected_url", [
    ("//button[@data-auto='decline']", REDIRECT_URL),
    ("//button[@data-auto='accept']", PRODUCT_URL)
])

@allure.feature('Check 18+ notification')
def test_age_confirmation(browser, button_xpath, expected_url):
    """Проверка работы окна 18+ и редиректов."""
    browser.get(PRODUCT_URL)

    with allure.step('Ожидание появления всплывающего окна 18+'):
        popup = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "/marketfrontDynamicPopupLoader42/content/content"))
        )
        assert popup.is_displayed(), "Окно 18+ не появилось."

    with allure.step('Нажимаем на кнопку "Нет" или "Уже есть"'):
        button = browser.find_element(By.XPATH, button_xpath)
        button.click()

    with allure.step('Ожидание редиректа + сверяем что редирект верный'):
        WebDriverWait(browser, 10).until(EC.url_to_be(expected_url))
        assert browser.current_url == expected_url, "Редирект не сработал корректно."

@allure.feature('Check 18+ notification')
def test_content_access(browser):
    """Проверка доступа к контенту 18+ после подтверждения возраста."""
    browser.delete_all_cookies()

    browser.get(PRODUCT_URL)

    with allure.step('Ожидание появления всплывающего окна 18+'):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "/marketfrontDynamicPopupLoader42/content/content"))
        )

    # Подтверждаем возраст
    with allure.step('Подтверждаем возраст по кнопке "Уже есть"'):
        browser.find_element(By.XPATH, "//button[@data-auto='accept']").click()

    with allure.step('Проверяем, что контент 18+ загружен'): 
        content = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "/content/page/fancyPage/defaultPage/mediaViewerManager"))
        )
        assert content.is_displayed(), "Контент 18+ не загрузился после подтверждения возраста."
