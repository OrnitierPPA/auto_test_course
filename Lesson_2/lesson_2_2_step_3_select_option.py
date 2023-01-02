import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(num1, num2):
    return str(num1 + num2)
try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.XPATH, "//form//span[2]").text)
    num2 = int(browser.find_element(By.XPATH, "//form//span[4]").text)

    result = calc(num1, num2)

    result_select = browser.find_element(By.CSS_SELECTOR, f"[value='{result}']").click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()