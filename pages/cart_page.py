from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
