import pyautogui
import time
from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class FileUpload(BasePage):
    CHOOSE_FILE = "//button[@class='btn btn-secondary btn-choose']"
    RESET = "//button[@class='btn btn-warning btn-reset']"

    def upload_file(self, value):
        self._driver.find_element(By.XPATH, self.CHOOSE_FILE).click()
        time.sleep(2)
        pyautogui.write(value, interval=0.1)
        pyautogui.press('return')

    def upload_reset(self):
        self._driver.find_element(By.XPATH, self.RESET).click()