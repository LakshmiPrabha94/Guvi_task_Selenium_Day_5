# Importing necessary modules and classes
import pytest
from cookies import SauceDemoAutomation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def automation_instance():
    # Create an instance of SauceDemoAutomation
    automation = SauceDemoAutomation()
    yield automation
    # Initialize Firefox WebDriver using GeckoDriverManager to handle driver management
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # Set implicit wait to 10 seconds to handle dynamic page elements
    driver.implicitly_wait(10)
    # Teardown - close the browser
    automation.shutdown()

# Positive Test Case: Successful Login
def test_successful_login(automation_instance):
    url = "https://www.saucedemo.com/"
    automation_instance.driver.get(url)
    # Perform login
    automation_instance.login("standard_user", "secret_sauce")
    # Check if login was successful by verifying the presence of an element on the next page
    assert automation_instance.driver.title == "Swag Labs"

# Negative Test Case: Invalid Credentials
def test_invalid_credentials(automation_instance):
    url = "https://www.saucedemo.com/"
    automation_instance.driver.get(url)
    # Perform login with invalid credentials
    automation_instance.login("invalid_user", "invalid_password")
    # Check if error message is displayed
    error_message = automation_instance.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error_message.is_displayed()

# Negative Test Case: Logging out without Logging in
def test_logout_without_login(automation_instance):
    # Attempt logout without logging in
    automation_instance.logout()
    # Check if the login page is still displayed
    assert "https://www.saucedemo.com/" in automation_instance.driver.current_url


# Negative test case to verify accessing cookies before login
def test_fetch_cookies_without_login():
    automation = SauceDemoAutomation()
    # Attempting to fetch cookies without login
    with pytest.raises(Exception):
        automation.fetch_cookies()
    automation.shutdown()

# Positive Test Case: Fetching Cookies after Login
def test_fetch_cookies_after_login(automation_instance):
    url = "https://www.saucedemo.com/"
    automation_instance.driver.get(url)
    # Perform login
    automation_instance.login("standard_user", "secret_sauce")
    # Fetch cookies after login
    cookies_after_login = automation_instance.fetch_cookies()
    # Check if cookies are fetched successfully
    assert cookies_after_login is not None

# Positive Test Case: Fetching Cookies before Login
def test_fetch_cookies_before_login(automation_instance):
    # Fetch cookies before login
    cookies_before_login = automation_instance.fetch_cookies()
    # Check if cookies are fetched successfully
    assert cookies_before_login is not None