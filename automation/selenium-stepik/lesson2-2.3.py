import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

LINK = 'https://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    alert = browser.switch_to.alert
    alert.accept()

    y = browser.find_element(By.ID, 'input_value').text
    numb = calc(int(y))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(numb)

    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()
