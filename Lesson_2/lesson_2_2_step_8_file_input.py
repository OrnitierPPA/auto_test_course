import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with open("selenium.txt", "w") as file:
  pass
mydir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(mydir, "selenium.txt")

try: 
  link = "http://suninjuly.github.io/file_input.html"
  browser = webdriver.Chrome()
  browser.get(link)

  name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('Ivan')
  surname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('Petrov')
  email = browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('IvanPetrov@mail.ru')
  input_file = browser.find_element(By.XPATH, "//input[@id='file']").send_keys(file_path)
  submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
  time.sleep(10)
  browser.quit()
  os.remove(file_path)
