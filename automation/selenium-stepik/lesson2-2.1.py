from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = 'https://suninjuly.github.io/math.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    y = browser.find_element(By.ID, 'input_value').text
    y = int(y)
    a = calc(y)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(a)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    assert people_checked, "People radio is not selected by default"

    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']").click()
    
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()


finally:
    time.sleep(5)
    browser.quit()