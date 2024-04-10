# Automated Cookie Handling with Selenium

## Description
This repository contains a Python automation script that demonstrates cookie handling on the SauceDemo website using Selenium. The script performs various actions such as logging in, fetching cookies before and after login, and logging out. 
Additionally, a test script is provided to validate the functionality of the automation script through different test cases.

## Automation Script
The automation script is named cookies.py. It includes a class `SauceDemoCookieHandling` with methods to initialize the WebDriver, navigate to the SauceDemo page, log in, fetch cookies, log out and handle browser shutdown.

## Test Script
The test script test_cookies.py contains test cases written using pytest to validate the functionality of the automation script.

Test Cases:

Positive scenarios: Successful login, fetching cookies before login, fetching cookies after login and Length of Cookies Increases After Successful Login.

Negative scenarios: Invalid credentials, Logging out without Logging in, Attempting to Fetch Cookies without Logging in, Length of Cookies Remains Unchanged After Successful Login and Checking Length of Cookies After Failed Login Attempt.

## Requirements
- Python 3.12.0
- Selenium library
- GeckoDriverManager (for managing GeckoDriver for Firefox)
- Firefox browser

## Setup

1. Install dependencies:
    ```
    pip install selenium webdriver-manager pytest
    ```
2. Make sure you have Firefox browser installed.

## Usage
1. Set the URL of the Instagram profile you want to scrape in the `cookies.py` script.
2. Run the automation script using Python:
    ```
    python cookies.py
    ```
3. To run the test script:
    ```
    pytest test_cookies.py
    ```

