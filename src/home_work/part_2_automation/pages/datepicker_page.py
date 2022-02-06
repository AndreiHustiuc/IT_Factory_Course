from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class DatePicker(BasePage):
    DATEPICKER = 'datepicker'

    def select_date(self, value):
        self._driver.find_element(By.ID, self.DATEPICKER).send_keys(value, Keys.ENTER)
