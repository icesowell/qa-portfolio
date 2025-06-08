from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Smirnov")
    input3 = browser.find_element(By.XPATH, "//label[text()='Email*']//following-sibling::input")
    input3.send_keys("Smolov245@mail.ru")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text, "Текст не совпадает"
finally:
    # успеваем скопировать код за 3 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла