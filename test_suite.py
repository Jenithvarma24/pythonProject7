import pytest

from tests.testtimesheet import TestTimesheet


test_login_classes = pytest.mark.login

test_login_classes(TestTimesheet.test_timesheet_functionality)