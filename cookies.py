#Name: Lakshmi Prabha
#Program : 
"""
Visit the url, https://www.instagram.com/guviofficial/ 
Try to fetch the following using Python Selenium
1. Followers of the webpage
2. Following of the webpage 
"""
#Date : 03 April 2024
#Version: 1
#Python Version: 3.12.0


# Importing necessary modules and classes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

class SauceDemoAutomation:
    def __init__(self):
        # Initialize Firefox WebDriver using GeckoDriverManager to handle driver management
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # Set implicit wait to 10 seconds to handle dynamic page elements
        self.driver.implicitly_wait(10)

    def login(self, username, password):
        try:
            # Wait for the visibility of the username element and fill in the username
            username_locator = "user-name"
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, username_locator)))
            self.driver.find_element(by=By.ID, value=username_locator).send_keys(username)

            # Fill in the password
            password_locator = "password"
            self.driver.find_element(by=By.ID, value=password_locator).send_keys(password)

            # Click on the login button
            login_locator = "login-button"
            self.driver.find_element(by=By.ID, value=login_locator).click()
        except NoSuchElementException as e:
            # Handle the exception and print an error message
            print("Error : ", e)

    def logout(self):
        # Click on the menu button
        menu_locator = '//*[@id="react-burger-menu-btn"]'
        self.driver.find_element(by=By.XPATH, value=menu_locator).click()

        # Click on the logout button
        logout_locator = '//*[@id="logout_sidebar_link"]'
        self.driver.find_element(by=By.XPATH, value=logout_locator).click()

    def fetch_cookies(self):
        # Fetch and print cookies
        cookies = self.driver.get_cookies()
        print("Cookies:")
        for cookie in cookies:
            print(cookie)
        return cookies
    
    def run(self):
        self.driver.get(url)
        # Fetch cookies before login
        print("Cookies before login:")
        self.fetch_cookies()
        # Login
        print("Navigated to Saucedemo webpage!!!")
        self.login("standard_user", "secret_sauce")
        # Fetch cookies after login
        print("Welcome to Saucedemo!!!")
        print("Cookies after login:")
        self.fetch_cookies()
        # Logout
        self.logout()
        print("Logged out from the application.")
        print("Thank you for shopping with us! Have a great day!")
        # Fetch cookies after logout
        print("Cookies after logout:")
        self.fetch_cookies()
        

    def shutdown(self):
        # Close the browser
        self.driver.quit()

url = "https://www.saucedemo.com/"

# Create an instance of SauceDemoAutomation and run the automation
if __name__ == "__main__":
    automation = SauceDemoAutomation()
    automation.run()
    automation.shutdown()
