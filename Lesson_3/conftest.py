import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Firefox()
#     browser.maximize_window()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

