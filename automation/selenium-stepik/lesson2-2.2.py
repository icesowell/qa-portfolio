import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


LINK = 'https://suninjuly.github.io/selects2.html'


try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    a = browser.find_element(By.ID, 'num1').text
    b = browser.find_element(By.ID, 'num2').text
    sum_var = int(a) + int(b)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum_var))

    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()
