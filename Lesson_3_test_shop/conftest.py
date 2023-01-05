import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose "--language": ru or en')

@pytest.fixture(scope="function")
def browser(request):
    interface_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': interface_language})
    print("\nStart browser..")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nQuit browser..")
    browser.quit()
    
