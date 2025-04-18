@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Installing Playwright browsers...
playwright install

echo Running Behave tests...
behave --tags=@login --no-capture

echo Generating Allure Report...
allure serve allure-results
