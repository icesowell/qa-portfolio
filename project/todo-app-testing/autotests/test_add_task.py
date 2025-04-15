from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://todomvc.com/examples/react/dist/"

def test_add_task(browser):
    browser.get(URL)
    input_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "new-todo"))
    )
    input_field.send_keys("Test Task")
    input_field.send_keys(Keys.ENTER)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li"))
    )
    todos = browser.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert any("Test Task" in todo.text for todo in todos)
