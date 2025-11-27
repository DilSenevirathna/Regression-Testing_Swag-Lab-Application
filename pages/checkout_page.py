from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    BACK_HOME_BTN = (By.ID, "back-to-products")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_info(self, fname, lname, zip_code):
        self.enter_text(self.FIRST_NAME, fname)
        self.enter_text(self.LAST_NAME, lname)
        self.enter_text(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        WebDriverWait(self.driver, self.timeout).until(EC.url_contains("checkout-step-two"))
        element = self.find_element(self.FINISH_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.click(self.FINISH_BTN)
    
    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
