import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

LINK = "https://SunInJuly.github.io/execute_script.html"

def calc(y):
    return str(math.log(abs(12*math.sin(int(y)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    x = browser.find_element(By.ID, 'input_value').text
    numb = calc(int(x))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(numb)

    browser.execute_script("window.scrollTo(0, 100);")

    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']").click()
    
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()
    
    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()


finally:
    time.sleep(5)
    browser.quit()
