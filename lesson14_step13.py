import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(fill_required_fields("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "Should be equal phrases")

    def test_registration2(self):
        self.assertEqual(fill_required_fields("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "Should be equal phrases")


def fill_required_fields(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "div.form-group.first_class input[required]").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "div.form-group.second_class input[required]").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "div.form-group.third_class input[required]").send_keys("yulya@mail.ru")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    time.sleep(10)
    browser.quit()
    return welcome_text


if __name__ == "__main__":
    pytest.main()
