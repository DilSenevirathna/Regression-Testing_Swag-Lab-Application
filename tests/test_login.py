import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    
    # Verify we are on inventory page
    assert "inventory" in driver.current_url

@pytest.mark.login
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "wrong_password")
    
    error_msg = login_page.get_error_message()
    assert "Epic sadface" in error_msg

@pytest.mark.login
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.logout()
    
    # Verify we are back on login page
    assert login_page.find_element(login_page.LOGIN_BTN).is_displayed()
