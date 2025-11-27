# 🧪 Regression Test Suite – SauceDemo

Automated with **Selenium WebDriver + Pytest (Python)**

This repository contains a fully automated **Regression Testing Suite** for **[https://www.saucedemo.com](https://www.saucedemo.com)**, designed to validate key functionalities such as authentication flows and the complete purchase process.

---

## 📌 Overview

This project automates critical user paths using:

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)** architecture

The suite ensures that the core functionalities of SauceDemo remain stable after updates.

---

## ✅ Features Covered

### **1. Login Functionality**

* ✔ Valid login
* ✔ Invalid login
* ✔ Logout verification

### **2. End-to-End Purchase Flow**

A complete regression flow:
**Login → Add to Cart → Checkout → Finish Order**

---

## 🏗️ Project Structure

```
project/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py        # 3 login-related tests
│   └── test_e2e.py          # Full end-to-end purchase test
│
├── conftest.py              # Driver setup + screenshot on failure
├── requirements.txt
└── README.md
```

---

## 🧱 Page Object Model (POM)

All page actions are modularized into separate classes:

* **LoginPage** – Handles login/logout actions
* **InventoryPage** – Product listing actions
* **CartPage** – Cart interactions
* **CheckoutPage** – Checkout steps

This ensures clean, reusable, and maintainable test code.

---

## 🧪 Test Suite

### **Test Files**

* `test_login.py` → Contains **3 tests**
* `test_e2e.py` → Contains **1 full scenario test**

### **Execution Summary (Sample Output)**

```
tests\test_e2e.py .                               [ 25%]
tests\test_login.py ...                           [100%]
=========================================================
4 passed, 4 warnings in 51.55s
=========================================================
```

---

## 📊 HTML Test Report

HTML execution reports are generated using:

```
pytest --html=report.html
```

The report is saved in:

```
project/report.html
```

---

## ▶️ How to Run the Tests

### **1. Install Dependencies**

```
pip install -r requirements.txt
```

### **2. Run the Regression Test Suite**

```
pytest --html=report.html
```

An HTML report will be created in the project root.

---

## 🧷 Additional Notes

* ✔ **Screenshots on failures** are automatically captured via `conftest.py`.
* ✔ Ensure you have a compatible **WebDriver** installed (e.g., ChromeDriver).
* ✔ Recommended Python version: **3.9+**

---

## 📞 Contact

For any questions or improvements, feel free to open an issue or submit a pull request.

---

**⭐ If you find this useful, consider starring the repository!**
