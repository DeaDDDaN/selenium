import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

s = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, language):
    link = f"{language}/"
    browser.get(link)
    browser.implicitly_wait(5)
    text = browser.find_element(By.CSS_SELECTOR, ".textarea")
    answer = math.log(int(time.time()))
    text.send_keys(str(answer))
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "submit-submission"))
    )
    button.click()
    attemp = WebDriverWait(browser, 10).until(
        EC._element_if_visible((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    if attemp.text != "Correct!":
        print(attemp.text)
    assert attemp.text == "Correct!"


