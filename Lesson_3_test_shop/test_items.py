import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    add_cart = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']").click()
    alert_wait = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.alertinner p > a.btn"))
    ).click()
    
    if browser.find_element(By.CSS_SELECTOR, "div.row div.col-sm-4 h3 > a"):
        assert True
    else:
        assert False