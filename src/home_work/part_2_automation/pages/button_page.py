from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class Button(BasePage):
    PRIMARY = 'btn btn-lg btn-primary'
    SUCCESS = 'btn btn-lg btn-success'
    INFO = 'btn btn-lg btn-info'
    WARNING = 'btn btn-lg btn-warning'
    DANGER = 'btn btn-lg btn-danger'
    LINK = 'btn btn-lg btn-link'
    LEFT = 'Left'
    RIGHT = 'Right'
    MIDDLE = 'Middle'
    ONE = '1'
    TWO = '2'
    DROP_DOWN = 'btn btn-lg btn-primary dropdown-toggle'

    def click_primary_button(self):
        self._driver.find_element(By.CLASS_NAME, self.PRIMARY).click()

    def click_success_button(self):
        self._driver.find_element(By.CLASS_NAME, self.SUCCESS).click()

    def click_info_button(self):
        self._driver.find_element(By.CLASS_NAME, self.INFO).click()

    def click_warning_button(self):
        self._driver.find_element(By.CLASS_NAME, self.WARNING).click()

    def click_danger_button(self):
        self._driver.find_element(By.CLASS_NAME, self.DANGER).click()

    def click_link_button(self):
        self._driver.find_element(By.CLASS_NAME, self.LINK).click()

    def click_left_button(self):
        self._driver.find_element(By.LINK_TEXT, self.LEFT).click()

    def click_middle_button(self):
        self._driver.find_element(By.LINK_TEXT, self.MIDDLE).click()

    def click_right_button(self):
        self._driver.find_element(By.LINK_TEXT, self.RIGHT).click()

    def click_1_button(self):
        self._driver.find_element(By.LINK_TEXT, self.ONE).click()

    def click_2_button(self):
        self._driver.find_element(By.LINK_TEXT, self.TWO).click()

    def click_dropdown_button(self):
        self._driver.find_element(By.LINK_TEXT, self.DROP_DOWN).click()
