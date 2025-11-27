import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.e2e
def test_purchase_flow(driver):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Add to Cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    
    # 3. Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    
    # 4. Fill Info
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Test", "User", "12345")
    
    # 5. Finish
    checkout_page.finish_checkout()
    
    # 6. Verify Success
    success_msg = checkout_page.get_complete_message()
    assert "Thank you for your order!" in success_msg
