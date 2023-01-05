import math
import pytest
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def answer():
    answer = math.log(int(time.time()))
    return answer

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize('link', links)
def test_login(browser, link):
    link = f"{link}"
    browser.get(link)
    wait_for_login = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.ID, 'ember33'))
    )
    login_button = browser.find_element(By.ID, 'ember33').click()
    input_email = browser.find_element(By.ID, 'id_login_email').send_keys('associatedtolife@mail.ru')
    input_password = browser.find_element(By.ID, 'id_login_password').send_keys('Arkaduy2131')
    submit = browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader ').click()

    wait_loading = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'stepik-loader__message'))
    )
    wait_loading = WebDriverWait(browser, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'stepik-loader__message'))
    )

    try:
        hint = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
        assert hint.text == 'Correct!', f"{hint.text}"
    except NoSuchElementException:
        text = browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']").send_keys(answer())
        submit = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        ).click()
        
        wait_hint = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        )
        hint = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')

        assert hint.text == 'Correct!', f"{hint.text}"