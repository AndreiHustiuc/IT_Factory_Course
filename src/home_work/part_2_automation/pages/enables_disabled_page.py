from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class EnabledDisabled(BasePage):
    INPUT_ID = 'input'

    def enter_text(self, value):
        self._driver.find_element(By.ID, self.INPUT_ID).send_keys(value)
