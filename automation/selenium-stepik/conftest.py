import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    print("\n start browser for test..")
    browser = webdriver.Firefox()
    yield browser
    # этот код выполнится после завершения теста
    print("\n quit browser..")
    browser.quit()

