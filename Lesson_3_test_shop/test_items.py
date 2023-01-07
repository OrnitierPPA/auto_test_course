from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    assert browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"), "No basket button"

    # Дальше дополнительная проверка, что товар добавился в корзину
    browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']").click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.alertinner p > a.btn"))
    ).click()
    
    assert browser.find_element(By.CSS_SELECTOR, "div.row div.col-sm-4 h3 > a"), "busket is empty"
