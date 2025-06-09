import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestselectorsCSS(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def test_search_in_python_org(self):

        browser = self.browser
        browser.get('http://suninjuly.github.io/registration1.html')
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Maryshev")
        input3 = browser.find_element(By.XPATH, "//label[text()='Email*']//following-sibling::input")
        input3.send_keys("Smolensk@mail.ru")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Текст не совпадает")
    
    def test_search2_in_python_org(self):

        browser = self.browser
        browser.get('http://suninjuly.github.io/registration2.html')
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Maryshev")
        input3 = browser.find_element(By.XPATH, "//label[text()='Email*']//following-sibling::input")
        input3.send_keys("Smolensk@mail.ru")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Текст не совпадает")

if __name__ == "__main__":
    unittest.main()

