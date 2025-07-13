
# 🧪 SauceDemo Automated Test Suite (Selenium + Python)

This repository contains an automated test suite for the https://www.saucedemo.com using **Selenium Edge WebDriver**, **Pytest**, and **Pytest-HTML**.

---

## 📦 Features

- Automated functional and UI testing
- Structured using **Page Object Model (POM)**
- Test execution via **Pytest**
- **HTML report** generation
- CI/CD compatible (e.g. GitHub Actions)

---

## ✅ Prerequisites

Make sure the following are installed:

| Tool    | Version (Minimum) |
|---------|-------------------|
| Python  | 3.8+              |
| pip     | Latest            |
| Edge    | Latest browser    |
| Github  | Any               |

You must also install the correct **EdgeDriver** matching your browser version.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:selviskmsc/SA-QA-Selvi-Senthil.git
cd SA-QA-Selvi-Senthil
```

### 2. Create and Activate Virtual Environment (Recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If any error in `requirements.txt`, install manually:
```bash
pip install selenium pytest pytest-html
```

---

## ▶️ Running the Test Suite

### Basic Test Execution

```bash
pytest tests/
```

### Run with HTML Report

```bash
pytest -s -v --html=Reports\report.html testcases/test_login.py --browser edge
pytest -s -v --html=Reports\report.html testcases/test_purchaseproduct.py --browser edge
pytest -s -v --html=Reports\report.html testcases/test_addtocart.py --browser edge
pytest -s -v --html=Reports\report.html testcases/test_shoppingcart.py --browser edge
pytest -s -v --html=Reports\report.html testcases/test_checkout.py --browser edge
pytest -s -v --html=Reports\report.html testcases/test_continuepurchase.py --browser edge
pytest -s -v --html=Reports\report.html testcases/test_finishpurchase.py --browser edge


```

### Sample Output Directory Structure
```
SA-QA-Selvi-Senthil/
├── Reports/
│   └── report.html    ← HTML report
```

---

## 🧪 Example Directory Layout

```
SA-QA-Selvi-Senthil/
├── pagesObjects/
│   ├── LoginPage.py
│   ├── AddtoCart.py
│   ├── Checkout.py
│   ├── Continue.py
│   ├── PurchaseProduct.py
│   └── FinishPurchase.py
├── tests/
│   ├── test_loginPage.py
│   ├── test_addtoCart.py
│   ├── test_checkout.py
│   ├── test_continue.py
│   ├── test_purchaseProduct.py
│   └── test_finishPurchase.py
├── reports/
│   └── test_report.html
├── requirements.txt
```

---

## 🧑‍💻 CI/CD Integration (GitHub Actions)

### Path: `.github/workflows/test.yml`

```yaml
name: Run Selenium Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests with HTML report
        run: |
          pytest tests/ --html=report.html --self-contained-html

      - name: Upload test report
        uses: actions/upload-artifact@v3
        with:
          name: selenium-report
          path: report.html
```

---

## 📝 Notes

- ✅ Tests run in **headless mode** by default in CI/CD.
- 📄 HTML reports are stored in the `reports/` folder (locally) or uploaded as artifacts (in CI).

---
