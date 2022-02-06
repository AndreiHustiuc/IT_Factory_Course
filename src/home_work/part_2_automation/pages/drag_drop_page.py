from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class DragAndDrop(BasePage):
    IMAGE = '//img[@alt="Selenium logo"]'
    BOX = 'box'

    def drag_and_drop(self):

        source = self._driver.find_element(By.XPATH, self.IMAGE)
        target = self._driver.find_element(By.ID, self.BOX)
        action = ActionChains(self._driver)
        action.drag_and_drop(source, target).perform()
