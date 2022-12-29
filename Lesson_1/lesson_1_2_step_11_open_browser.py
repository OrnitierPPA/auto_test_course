import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


# Устанавливает самую новую версию драйвера и использует её
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
time.sleep(5)

# Запускает ссылку в браузере
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

# Нахлжиь текстовое поле, вставляет в него текст
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("get()")

# Гаходит кнопку подтверждения и кликает на неё
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()
time.sleep(5)

driver.quit()