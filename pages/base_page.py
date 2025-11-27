from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    def find_element(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Timeout waiting for element: {locator}")
            raise

    def click(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            print(f"Timeout waiting for element to be clickable: {locator}")
            raise

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
