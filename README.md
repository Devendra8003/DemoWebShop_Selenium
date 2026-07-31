# Demo Web Shop Selenium Automation Framework
![Selenium Tests](https://github.com/Devendra8003/DemoWebShop_Selenium/actions/workflows/selenium-tests.yml/badge.svg)

## Project Overview

This project is an End-to-End Selenium Automation Testing Framework developed using **Python**, **Selenium WebDriver**, **PyTest**, and the **Page Object Model (POM)** design pattern.

The framework automates major functionalities of the Demo Web Shop website and generates HTML execution reports.

Website Tested:

https://demowebshop.tricentis.com/

---

# Tech Stack

- Python 3.12
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- webdriver-manager
- pytest-html

---

# Project Structure

```
DemoWebShop_Selenium/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── search_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── review_page.py
│
├── utils/
│   ├── config.py
│   ├── driver_factory.py
│
├── test_login.py
├── test_logout.py
├── test_search.py
├── test_add_to_cart.py
├── test_cart.py
├── test_remove_cart.py
├── test_coupon.py
├── test_gift_card.py
├── test_compare_product.py
├── test_remove_compare.py
├── test_email_friend.py
├── test_product_review.py
├── test_product_details.py
├── test_checkout.py
├── test_shopping_cart.py
├── test_wishlist.py
│
├── conftest.py
├── requirements.txt
├── README.md
└── Report.html
```

---

# Features Automated

## Authentication

- Login (Valid Credentials)
- Login (Invalid Password)
- Login (Invalid Email)
- Logout

---

## Product

- Search Product
- Product Details
- Product Review
- Email a Friend

---

## Shopping Cart

- Add Product to Cart
- Shopping Cart Verification
- Remove Product from Cart
- Apply Coupon
- Gift Card Section

---

## Wishlist

- Add Product to Wishlist

---

## Compare Products

- Add Product to Compare List
- Remove Compared Products

---

## Checkout

- Complete Checkout Process
- Billing Address
- Shipping Address
- Shipping Method
- Payment Method
- Payment Information
- Order Confirmation

---

# Test Cases

| Test Case | Status |
|------------|--------|
| Login | ✅ |
| Logout | ✅ |
| Search Product | ✅ |
| Product Details | ✅ |
| Add To Cart | ✅ |
| Shopping Cart | ✅ |
| Remove Cart | ✅ |
| Coupon | ✅ |
| Gift Card | ✅ |
| Wishlist | ✅ |
| Compare Product | ✅ |
| Remove Compare Product | ✅ |
| Email Friend | ✅ |
| Product Review | ✅ |
| Checkout | ✅ |

**Total Test Cases:** 18

**Passed:** 18

**Failed:** 0

---

# Installation

Clone the repository

```bash
git clone https://github.com/YourGitHubUsername/DemoWebShop_Selenium.git
```

Move into project folder

```bash
cd DemoWebShop_Selenium
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run Individual Test

Example

```bash
python -m pytest test_login.py -v -s
```

---

# Run Complete Test Suite

```bash
python -m pytest -v
```

---

# Generate HTML Report

```bash
python -m pytest -v --html=Report.html --self-contained-html
```

The HTML report will be generated as:

```
Report.html
```

Open it in any web browser to view the execution results.

---

# Design Pattern

This project follows the **Page Object Model (POM)** architecture.

Benefits:

- Reusable code
- Easy maintenance
- Better readability
- Reduced duplication
- Scalable automation framework

---

# Tools Used

- Selenium WebDriver
- PyTest
- webdriver-manager
- pytest-html
- Chrome Browser
- Visual Studio Code
- Git
- GitHub

---

# Project Results

```
===========================
18 Tests Executed
18 Passed
0 Failed
Execution Time:
7 Minutes 09 Seconds
===========================
```

---

# Future Enhancements

- Jenkins CI/CD Integration
- GitHub Actions
- Screenshot on Test Failure
- Logging Framework
- Cross Browser Testing
- Data Driven Testing
- Parallel Execution using pytest-xdist
- Allure Reporting

---

# Author

**Devendra Viswash**

Python Full Stack Developer | Selenium Automation Tester

GitHub:
https://github.com/Devendr8003

LinkedIn:
https://www.linkedin.com/in/devendra-vishwas-6712aa249

---

# License

This project is developed for learning, practice, and portfolio purposes.
