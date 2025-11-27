Regression Test Suite Walkthrough
Overview
I have successfully created a regression test suite for saucedemo.com using Selenium and Pytest. The suite covers:

Login functionality (valid/invalid/logout)
End-to-End Purchase Flow (Login -> Add to Cart -> Checkout -> Finish)
Implementation Details
Page Object Model: Implemented in pages/ directory.

LoginPage
, 

InventoryPage
, 

CartPage
, 

CheckoutPage
Tests: Implemented in tests/ directory.

test_login.py
: 3 tests

test_e2e.py
: 1 test
Configuration: 

conftest.py
 handles driver setup and screenshot capture on failure.
Verification Results
Ran the full test suite using pytest --html=report.html.

Test Summary
Total Tests: 4
Passed: 4
Failed: 0
Execution Output
tests\test_e2e.py .                                                                                                                                       [ 25%]
tests\test_login.py ...                                                                                                                                   [100%]
================================================================ 4 passed, 4 warnings in 51.55s ================================================================
Report
An HTML report has been generated at d:/Project/QA foriegn/report.html.

How to Run
Ensure dependencies are installed: pip install -r requirements.txt
Run tests: pytest --html=report.html
