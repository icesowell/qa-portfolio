from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math

LINK = "https://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    wait = WebDriverWait(browser, 10)
    var = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button = wait.until(EC.element_to_be_clickable((By.ID, "book"))).click()

    
    y = browser.find_element(By.ID, 'input_value').text
    numb = calc(int(y))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(numb)

    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally: 
    time.sleep(5)
    browser.quit()