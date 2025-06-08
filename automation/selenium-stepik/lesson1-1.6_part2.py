from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math

numb = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = 'http://suninjuly.github.io/find_link_text' 

try:
    #Первый блок задания, найти ссылку с текстом выражения из Numb
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, numb)
    link.click()

    #Второй блок, заполнить форму данными и получить ответ 
    wait = WebDriverWait(browser, 10)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="form-control city"]')))
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()