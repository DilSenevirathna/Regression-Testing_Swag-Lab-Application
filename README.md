🧪 Regression Test Suite for SauceDemo

Automated with Selenium + Pytest

📌 Overview

This project provides a fully automated regression test suite for saucedemo.com, built using Selenium WebDriver, Python, and Pytest.
The suite validates core functionality including authentication flows and the full purchase process.

✅ Features Covered
1. Login Functionality

Valid login

Invalid login

Logout verification

2. End-to-End Purchase Flow

(Login → Add to Cart → Checkout → Finish)

🏗️ Implementation Details
📂 Project Structure
project/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py      # contains 3 login-related tests
│   └── test_e2e.py        # contains full E2E purchase test
│
├── conftest.py            # driver setup + screenshot on failure
├── requirements.txt
└── README.md

Page Object Model (POM)

All page interactions are organized following the POM pattern:

LoginPage

InventoryPage

CartPage

CheckoutPage

Test Files

test_login.py → 3 tests

test_e2e.py → 1 full scenario test

📊 Test Execution Summary

Executed using:

pytest --html=report.html

Results

Total Tests: 4

Passed: 4

Failed: 0

Example Output
tests\test_e2e.py .                               [ 25%]
tests\test_login.py ...                           [100%]
=========================================================
4 passed, 4 warnings in 51.55s
=========================================================

HTML Test Report

Generated at:

d:/Project/QA foreign/report.html

▶️ How to Run the Tests
1. Install Dependencies
pip install -r requirements.txt

2. Execute Test Suite
pytest --html=report.html


An HTML report will be generated in the project directory.

🧷 Notes

Screenshots on test failure are automatically captured via conftest.py.

Make sure you have a compatible WebDriver (e.g., ChromeDriver) installed and properly configured.
