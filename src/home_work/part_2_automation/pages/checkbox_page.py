from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class CheckBox(BasePage):
    CHECKBOX_1 = 'checkbox-1'
    CHECKBOX_2 = 'checkbox-2'
    CHECKBOX_3 = 'checkbox-3'

    def click_on_checkbox_1(self):
        self._driver.find_element(By.ID, self.CHECKBOX_1).click()

    def click_on_checkbox_2(self):
        self._driver.find_element(By.ID, self.CHECKBOX_2).click()

    def click_on_checkbox_3(self):
        self._driver.find_element(By.ID, self.CHECKBOX_3).click()
