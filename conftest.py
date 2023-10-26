import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def base_url():
    return "https://aspire.atmecs.online/login"

@pytest.fixture(scope="session")
def timesheet_data():
    return {
        "email": "jenith.ravichandran@atmecs.com",
        "password": "Jenithvarma@123",
        "text": "I worked on all the five days",
        "activity": "Learning & Development",
        "values": [9, '', 9, 9, 9]
    }

@pytest.fixture(scope="session", autouse=True)
def browser_setup():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    # driver.quit()