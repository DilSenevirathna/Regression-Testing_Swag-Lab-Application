from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def logout(self):
        self.click(self.BURGER_MENU)
        # Wait for animation or visibility if needed, but click handles wait
        self.click(self.LOGOUT_LINK)
