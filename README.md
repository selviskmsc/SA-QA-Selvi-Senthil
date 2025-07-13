
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
git clone 
cd saucedemo-automation
```

### 2. Create and Activate Virtual Environment (Recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
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
pytest tests/ --html=reports/test_report.html --self-contained-html
```

### Sample Output Directory Structure
```
saucedemo_automation/
├── reports/
│   └── test_report.html    ← HTML report
```

---

## 🧪 Example Directory Layout

```
saucedemo_automation/
├── pages/
│   ├── login_page.py
│   └── product_page.py
├── tests/
│   ├── test_login.py
│   └── test_cart.py
├── reports/
│   └── test_report.html
├── conftest.py
├── requirements.txt
├── pytest.ini (optional)
```

---

## 🧑‍💻 CI/CD Integration (GitHub Actions)

### Path: `.github/workflows/test.yml`

```yaml
name: Run Selenium Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

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

## 🤝 Contributing

Feel free to fork, raise issues, or contribute test cases!
