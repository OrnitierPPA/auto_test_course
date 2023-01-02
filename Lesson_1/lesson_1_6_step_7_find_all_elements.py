import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

value=["Да", "Конечно", "Нет", "Отнюдь", "Естественно", "Ясен-красен", "Вовсе нет!"]
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(random.choice(value))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла