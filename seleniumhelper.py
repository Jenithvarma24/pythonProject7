import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def element_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def element_enter(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def element_is_present(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return True
        except Exception as exception:
            print(f"Not present: {exception}")

    def is_title(self, expected_title, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements(self, locator):
        wait = WebDriverWait(self.driver, 30)
        elements = wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def find_element(self, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_clear(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.clear()
        except Exception as e:
            pytest.fail(f"An error occurred while clearing the element {locator}: {e}")

    def scroll_into(self, element):
        try:
            # Check if the element is present and visible before scrolling
            if element.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            else:
                print("Element is not visible, skipping scroll.")
        except Exception as e:
            print(f"An error occurred while scrolling: {e}")

    def get_element_attribute(self, locator, attribute):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            attribute_value = element.get_attribute(attribute)
            return attribute_value
        except Exception as e:
            raise Exception(f"Failed to get element attribute: {e}")

    def get_element_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            element_text = element.text
            return element_text
        except Exception as e:
            raise Exception(f"Failed to get element text: {e}")

    def is_element_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception as e:
            raise Exception(f"Failed to display element: {e}")

    def wait_for_element_to_be_present(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except Exception as exception:
            print(f"Not present: {exception}")
