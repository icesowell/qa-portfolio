import pytest
from pages.login_page import LoginPage
from pages.lesson_page import LessonPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_correct_answer(browser, link):
    login = LoginPage(browser)
    lesson = LessonPage(browser)
    base = BasePage(browser)

    login.open(link)
    login.login("username", "pass")
    print("Логин отработал")

    base.wait_for_page_loaded()
    lesson.submit_answer()
    print("Сабмит нажат")

    feedback = lesson.get_feedback()
    print("фидбек забрали")

    print(f"\nОтвет: 'Correct!' — результат: {feedback}")
    assert "Correct!" in feedback, f"\nОжидалось Correct!, а получено: {feedback}"
