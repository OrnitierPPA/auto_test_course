import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    math_test = browser.find_element(By.ID, "answer")
    math_test.send_keys(y)

    i_am_robot = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']").click()
    robots_rule = browser.find_element(By.XPATH, "//label[@for='robotsRule']").click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
