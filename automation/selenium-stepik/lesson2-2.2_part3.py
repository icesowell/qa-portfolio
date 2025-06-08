import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 


LINK = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    wait = WebDriverWait(browser, 10)

    input_first_name = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]').send_keys("Ivan")
    input_last_name = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]').send_keys("Petrov")
    input_email = browser.find_element(By.CSS_SELECTOR, '[name = "email"]').send_keys("армани_джинс@dasha288.play")



    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)

    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

finally:
    time.sleep(5)
    browser.quit()