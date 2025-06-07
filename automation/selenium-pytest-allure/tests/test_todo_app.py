"""
icesowell 2025
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://todomvc.com/examples/react/dist/"

@allure.title("Добавление новой задачи")
@allure.description("Проверяем, что задача успешно добавляется и отображается в списке")
def test_add_task(browser):
    browser.get(URL)
    with allure.step("Вводим текст задачи"):
        input_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
        )
        input_field.send_keys("Test Task")
        input_field.send_keys(Keys.ENTER)

    with allure.step("Проверяем, что задача добавилась"):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li"))
        )
        todos = browser.find_elements(By.CSS_SELECTOR, ".todo-list li")
        assert any("Test Task" in todo.text for todo in todos)

@allure.title("Создание задачи из пробелов")
def test_create_task_with_spaces(browser):
    browser.get(URL)
    with allure.step("Вводим пробелы в поле задачи"):
        input_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
        )
        input_field.send_keys("     ")
        input_field.send_keys(Keys.ENTER)

    with allure.step("Проверяем, что задача не создалась"):
        WebDriverWait(browser, 3).until(
            lambda b: len(b.find_elements(By.CSS_SELECTOR, ".todo-list li")) == 0
        )
        todos = browser.find_elements(By.CSS_SELECTOR, ".todo-list li")
        assert len(todos) == 0

@allure.title("Завершение задачи")
def test_complete_task_marks_it_completed(browser):
    browser.get(URL)
    with allure.step("Добавляем задачу"):
        input_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
        )
        input_field.send_keys("Complete me")
        input_field.send_keys(Keys.ENTER)

    with allure.step("Отмечаем задачу завершенной"):
        checkbox = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".toggle"))
        )
        checkbox.click()

    with allure.step("Проверяем, что задача стала завершённой"):
        completed = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".completed"))
        )
        assert "Complete me" in completed.text

@allure.title("Редактирование задачи")
def test_edit_task_and_save_with_enter(browser):
    browser.get(URL)
    with allure.step("Создаём задачу"):
        input_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
        )
        input_field.send_keys("Old Name")
        input_field.send_keys(Keys.ENTER)

    with allure.step("Редактируем задачу"):
        todo_item = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li"))
        )
        label = todo_item.find_element(By.CSS_SELECTOR, "label")
        browser.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('dblclick', { bubbles: true }));",
            label
        )

        edit_input = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#todo-input"))
        )
        edit_input.clear()
        edit_input.send_keys("New Name")
        edit_input.send_keys(Keys.ENTER)

    with allure.step("Проверяем, что задача изменилась"):
        todos = browser.find_elements(By.CSS_SELECTOR, ".todo-list li")
        assert any("New Name" in todo.text for todo in todos)

@allure.title("Удаление завершённой задачи через кнопку Clear Completed")
def test_clear_completed_removes_completed_tasks(browser):
    browser.get(URL)
    with allure.step("Создаём и завершаем задачу"):
        input_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
        )
        input_field.send_keys("To Complete")
        input_field.send_keys(Keys.ENTER)

        checkbox = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".toggle"))
        )
        checkbox.click()

    with allure.step("Удаляем завершённую задачу"):
        clear_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "clear-completed"))
        )
        clear_button.click()

    with allure.step("Проверяем, что задача удалена"):
        WebDriverWait(browser, 3).until(
            lambda b: len(b.find_elements(By.CSS_SELECTOR, ".todo-list li")) == 0
        )
        todos = browser.find_elements(By.CSS_SELECTOR, ".todo-list li")
        assert len(todos) == 0

@allure.title("Фильтрация по активным задачам")
def test_filter_active_shows_only_active_tasks(browser):
    browser.get(URL)
    with allure.step("Добавляем две задачи"):
        input_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
        )
        input_field.send_keys("Active Task")
        input_field.send_keys(Keys.ENTER)
        input_field.send_keys("Completed Task")
        input_field.send_keys(Keys.ENTER)

    with allure.step("Завершаем одну из задач"):
        checkboxes = browser.find_elements(By.CSS_SELECTOR, ".toggle")
        checkboxes[1].click()

    with allure.step("Переходим к фильтру 'Active'"):
        active_filter = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Active"))
        )
        active_filter.click()

    with allure.step("Проверяем, что отобразилась только активная задача"):
        WebDriverWait(browser, 3).until(
            lambda b: len(b.find_elements(By.CSS_SELECTOR, ".todo-list li")) == 1
        )
        todos = browser.find_elements(By.CSS_SELECTOR, ".todo-list li")
        assert todos[0].text == "Active Task"
