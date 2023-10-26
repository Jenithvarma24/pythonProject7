import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper.seleniumhelper import SeleniumHelper


class Timesheetpage(SeleniumHelper):

    timesheet = (By.XPATH, '(//a[@class="sidebar-link"])[6]')
    previous_left = (By.XPATH, '//span[@class="fa fa-caret-left "]')
    previous_right = (By.XPATH, '//span[@class="fa fa-caret-right"]')
    notes = (By.XPATH, '//button[@class="notes-pop btn btn-sm btn-info"]')
    text = (By.XPATH, '(//div[@class="form-group"]//following::textarea[@class="form-control notetext"])[2]')
    text_ok_button = (By.XPATH, '(//button[@class="btn btn-sm btn-primary save-notes"])[2]')
    add_activity = (By.XPATH, '//button[@class="addmore btn btn-sm btn-success "]')
    activity_delete = (By.XPATH, '//button[@class="removefield btn btn-sm btn-danger"]')
    hours = (By.XPATH, '//td[@class=" workhourstd"]//input')
    drop_down_button = (By.XPATH, '//span[@class="select2-selection__arrow"]')
    drop_down_button2 = (By.XPATH, '(//span[@class="select2-selection__arrow"])[2]')
    leave = (By.XPATH, '//li[text()="Leave"]')
    activity = (By.XPATH, '//li[@class="select2-results__option"]')
    save = (By.XPATH, '//a[text()="Save"]')
    submit_button = (By.XPATH, '//a[text()="Submit for Approval"]')
    ok_button = (By.XPATH, '//div[@class="modal-content"]/div[@class="modal-footer"]/button')
    leave_hours0 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[7]')
    leave_hours1 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[8]')
    leave_hours2 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[9]')
    leave_hours3 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[10]')
    leave_hours4 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[11]')
    approve = (By.XPATH, '//span[text()="Approved"]')

    def test_timesheet(self, text):
        try:
            self.element_click(self.timesheet)
            self.element_click(self.previous_left)
            element = self.find_element(self.approve)
            assert element.text == "Approved"

            if element.text == "Approved":
                print("The lastweek timesheet is approved.")

            self.element_click(self.previous_right)
            self.element_click(self.notes)
            self.element_enter(self.text, text)
            self.element_click(self.text_ok_button)
        except Exception as e:
            pytest.fail(f"An error occurred in test_timesheet: {e}")

    def choose_activity_by_text(self, activity):
        try:
            self.element_click(self.drop_down_button)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.activity))
            dropdown_elements = self.driver.find_elements(*self.activity)

            for element in dropdown_elements:
                if element.text == activity:
                    element.click()
                    break
        except Exception as e:
            pytest.fail(f"An error occurred in choose_activity_by_text: {e}")
    def filling_timesheet_hours(self, values):
        try:
            index_of_zero = values.index(0)
            print(f"The value 0 is at index {index_of_zero}.")
        except ValueError:
            print("The value 0 is not present in the list.")
            index_of_zero = -1

        elements = self.find_elements(self.hours)

        for i, element in enumerate(elements):
            value_to_insert = values[i]
            element.send_keys(value_to_insert)

        if index_of_zero == -1:
            self.element_click(self.save)
            if index_of_zero < 9:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.invisibility_of_element_located((By.ID, "alertPopup")))
                self.element_click(self.ok_button)
        else:
            wait = WebDriverWait(self.driver, 10)
            add = wait.until(EC.element_to_be_clickable(self.add_activity))
            add.click()

            wait = WebDriverWait(self.driver, 10)
            drop2 = wait.until(EC.element_to_be_clickable(self.drop_down_button2))
            drop2.click()
            self.element_click(self.leave)

            if index_of_zero == 0:
                self.scroll_into(self.leave_hours0)
                self.element_click(self.leave_hours0)
                self.element_clear(self.leave_hours0)
                self.element_enter(self.leave_hours0, "L")
            elif index_of_zero == 1:
                self.scroll_into(self.leave_hours1)
                self.element_click(self.leave_hours1)
                self.element_clear(self.leave_hours1)
                self.element_enter(self.leave_hours1, "L")
            elif index_of_zero == 2:
                self.scroll_into(self.leave_hours2)
                self.element_click(self.leave_hours2)
                self.element_clear(self.leave_hours2)
                self.element_enter(self.leave_hours2, "L")
            elif index_of_zero == 3:
                self.scroll_into(self.leave_hours3)
                self.element_click(self.leave_hours3)
                self.element_clear(self.leave_hours3)
                self.element_enter(self.leave_hours3, "L")
            elif index_of_zero == 4:
                self.scroll_into(self.leave_hours4)
                self.element_click(self.leave_hours4)
                self.element_clear(self.leave_hours4)
                self.element_enter(self.leave_hours4, "L")
            else:
                print("There is no 0 is present")
                self.element_click(self.save)
                self.element_click(self.ok_button)