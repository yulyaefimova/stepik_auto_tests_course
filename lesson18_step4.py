import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()


class TestStepikPage:
    str = ""
    urls = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

    @pytest.mark.parametrize('url', urls)
    def test_registration(self, browser, url):
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)
        browser.find_element(By.ID, "ember33").click()
        browser.find_element(By.ID, "id_login_email").send_keys("логин stepik")
        browser.find_element(By.ID, "id_login_password").send_keys("пароль")
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()

        elements = browser.find_elements(By.CSS_SELECTOR, ".again-btn.white")
        if elements:
            elements[0].click()
        textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
        textarea.click()
        textarea.send_keys(str(math.log(int(time.time() - 0.9))))
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        answer = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        assert answer == "Correct!", "Wrong answer"


if __name__ == "__main__":
    pytest.main()
