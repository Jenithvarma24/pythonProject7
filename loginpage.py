from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper.seleniumhelper import SeleniumHelper
import time



class LoginPage(SeleniumHelper):
    email_input = (By.XPATH, '//input[@type="email"]')
    password_input = (By.XPATH, '//input[@type="password"]')
    login_button = (By.XPATH, '//input[@id="submitbtn"]')
    profile_button = (By.XPATH, '//li[@class="nav-item dropdown"]')
    logout_button = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver):
        self.driver = driver

    def test_aspire_login(self, email, password):
        self.element_enter(self.email_input, email)
        self.element_enter(self.password_input, password)
        time.sleep(10)

        self.element_click(self.login_button)

        login_success = self.wait_for_element_to_be_present(self.profile_button, timeout=5)
        assert login_success, "Login was not successful"

    def test_logout(self, email, password):
        user_input = input("Do you want to log out? (yes/no): ")
        if user_input.lower() == 'yes':
            profile_button = self.is_element_displayed(self.profile_button)
            assert profile_button, "Profile dropdown button is not displayed"
            self.element_click(self.profile_button)

            logout_success = self.is_element_displayed(self.logout_button)
            assert logout_success, "Logout was not successful"
            self.element_click(self.logout_button)

            user_input2 = input("Do you want to login again? (yes/no): ")
            if user_input2.lower() == 'yes':
                self.test_aspire_login(email, password)  # Log in again with email and password
            elif user_input2.lower() == 'no':
                print("Just stay out.")
            else:
                print("Invalid input. Please enter 'yes' or 'no.")

        elif user_input.lower() == 'no':
            print("Just stay in.")
        else:
            print("Invalid input. Please enter 'yes' or 'no.")