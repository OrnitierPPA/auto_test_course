import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    start = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    new_window_switch = browser.switch_to.window(new_window)

    value = browser.find_element(By.ID, 'input_value').text
    result = calc(value)
    string = browser.find_element(By.NAME, 'text').send_keys(result)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()
