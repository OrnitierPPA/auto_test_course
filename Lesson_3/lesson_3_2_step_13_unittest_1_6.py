import unittest 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):
    global expected_welcome_text 
    expected_welcome_text  = "Congratulations! You have successfully registered!"

    def form(self, link):
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link)

        button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
            )

        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input2 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']/input")
        input2.send_keys("Petrov@mail.ru")

        button.click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1")

        return welcome_text.text

    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        result = self.form(link)

        self.assertEqual(expected_welcome_text, result, f"Should be '{expected_welcome_text}', but '{result}'")

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        result = self.form(link)

        self.assertEqual(expected_welcome_text, result, f"Should be '{expected_welcome_text}', but '{result}'")
    
    def quit_driver(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
