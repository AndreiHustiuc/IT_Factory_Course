from selenium.webdriver.common.by import By

from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class DropDown(BasePage):
    DROP_DOWN_ID = 'dropdownMenuButton'

    def select_from_dropdown(self, value):
        self._driver.find_element(By.ID, self.DROP_DOWN_ID).click()
        self._driver.find_element(By.LINK_TEXT, value).click()
