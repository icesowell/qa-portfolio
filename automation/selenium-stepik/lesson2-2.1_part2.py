from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = 'https://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    y = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    y = int(y)
    a = calc(y)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(a)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox").click()
    
    radiobutton1 = browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()


finally:
    time.sleep(5)
    browser.quit()