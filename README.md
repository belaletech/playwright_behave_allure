# Playwright + Behave + Allure Integration

This project integrates **Playwright** with **Behave (BDD framework)** and **Allure Reporting** for automated testing on **LambdaTest's cloud grid**.

---

## 📂 Project Structure
```
playwright_behave_allure/
│── features/
│   ├── login.feature
│   ├── steps/
│   │   ├── login_steps.py
│── tests/
│   ├── conftest.py
│── pages/
│   ├── login_page.py
│── allure-results/
│── behave.ini
│── config.json
│── pytest.ini
│── requirements.txt
│── run_tests.bat
│── README.md
```

---

## 🚀 Prerequisites

1. **Python 3.8+** installed
2. **Google Chrome** installed
3. Install **pip & virtualenv**
   ```sh
   pip install --upgrade pip
   pip install virtualenv
   ```
4. Install **Allure CLI** (for report generation)
   ```sh
   choco install allure
   ```
   *(Requires [Chocolatey](https://chocolatey.org/install))*

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```sh
cd D:\USER\
git clone https://github.com/your-repo/playwright_behave_allure.git
cd playwright_behave_allure
```

### 2️⃣ Create and Activate Virtual Environment
```sh
python -m venv venv
venv\Scripts\activate  (For Windows)
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Install Playwright Browsers
```sh
playwright install
```

### 5️⃣ Set Environment Variables (For LambdaTest Integration)
```sh
set LT_USERNAME=your_username
set LT_ACCESS_KEY=your_access_key
set HEROKU_USERNAME=your_heroku_email
set HEROKU_PASSWORD=your_heroku_password
```

*(Or permanently add these to System Environment Variables)*

---

## ▶️ Running Tests

### **Run All Tests**
```sh
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```



## 📊 Viewing Test Reports
After running tests, generate and view an **Allure Report**:
```sh
allure serve allure-results
```

This should open the Allure report in your browser.

---

## 📌 Notes
- Ensure **Chrome** and **Python 3.8+** are installed.
- Use **LambdaTest credentials** in `LT_USERNAME` and `LT_ACCESS_KEY`.
- If the `allure` command is not recognized, install via Chocolatey.

---

### 🎯 Happy Testing! 🚀

