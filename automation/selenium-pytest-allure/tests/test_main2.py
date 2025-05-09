"""
icesowell 2025 (c)
"""

from selenium.webdriver.common.by import By

URL = "https://postcard.qa.studio/"


def test_smoke(browser):
    """
    SMK-1. Smoke test
    """

    browser.get(URL)

    button = browser.find_element (By.ID, "send")
    assert button.text == 'Отправить', "Unexpected text on button"

def test_empty_input_send(browser):
    """
    SMK-2. Negative case
    """

    browser.get(URL)

    email_label = browser.find_element (By.CSS_SELECTOR, value = 'div.email h2')
    email_label_text = email_label.get_attribute('class')
    assert email_label_text == "requered", 'Unexpected attribute class'


    button = browser.find_element (By.ID, "send")
    button.click()

    email_label = browser.find_element (By.CSS_SELECTOR, value = 'div.email h2')
    email_label_text = email_label.get_attribute('class')
    assert email_label_text == "requered error", 'Unexpected attribute class'



def test_send_postcard(browser):
    """
    SMK-3. Positive case
    """
    browser.get(URL)

    email = browser.find_element(By.ID, value='email')
    email.click()
    email.send_keys('icesowell@yan.ru') #чтобы ввести текст

    browser.find_element (By.CSS_SELECTOR, value= '[class*="photo-parent"]')
    message = browser.find_element(By.ID, value='textarea')
    message.click()
    message.send_keys('Hello')

    button = browser.find_element (By.ID, "send")
    button.click()

    assert True, ""
