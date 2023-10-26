import pytest
from pages.timesheetpage import Timesheetpage
from pages.loginpage import LoginPage

class TestTimesheet:

    @pytest.fixture(autouse=True)
    def setup_class(self, browser_setup, base_url, timesheet_data):
        self.driver = browser_setup
        self.driver.get(base_url)

        self.login_page = LoginPage(self.driver)
        self.timesheet_page = Timesheetpage(self.driver)
        self.email = timesheet_data["email"]
        self.password = timesheet_data["password"]
        self.text = timesheet_data["text"]
        self.values = timesheet_data["values"]
        self.activity = timesheet_data["activity"]

    @pytest.mark.login
    def test_timesheet_functionality(self):
        try:
            # Login
            self.login_page.test_aspire_login(self.email, self.password)
            self.login_page.test_logout(self.email,self.password)
            self.timesheet_page.test_timesheet(self.text)
            self.timesheet_page.choose_activity_by_text(self.activity)
            self.timesheet_page.filling_timesheet_hours(self.values)

        except Exception as e:
            pytest.fail(f"An error occurred: {e}")