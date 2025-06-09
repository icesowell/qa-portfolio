from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import math
import time

class LessonPage(BasePage):
    TEXTAREA = (By.CSS_SELECTOR, "textarea")
    SUBMIT_BTN = (By.CSS_SELECTOR, ".submit-submission")
    HINT = (By.CSS_SELECTOR, ".smart-hints__hint")

    def submit_answer(self):
        answer = str(math.log(int(time.time())))
        self.send_keys(self.TEXTAREA, answer)
        print("Текст был введен")
        self.click(self.SUBMIT_BTN)
        print("Кнопка была нажата")

    def get_feedback(self):
        return self.get_text(self.HINT)
        
