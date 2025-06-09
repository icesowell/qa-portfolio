from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)
        self.timeout = timeout

    def open(self, url):
        self.browser.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value, clear_first=True):
        element = self.wait.until(EC.presence_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_for_page_loaded(self,):
        WebDriverWait(self.browser, self.timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
