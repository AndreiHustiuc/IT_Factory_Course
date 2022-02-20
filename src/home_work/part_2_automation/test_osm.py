import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class OpenStreetMap(unittest.TestCase):

    SEARCH_BAR = (By.CSS_SELECTOR, '#sidebar #query')
    GO_BUTTON = (By.CSS_SELECTOR, "#sidebar .col .btn")
    SELECT_CITY = (By.XPATH, '//a[@data-prefix="City"]')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='..\\part_2_automation\\drivers\\chromedriver.exe')
        self.driver.get('https://master.apis.dev.openstreetmap.org/')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def find_one_city(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('Timisoara')
        self.driver.find_element(*self.GO_BUTTON).click()
        time.sleep(3)

        actual_value = self.driver.find_element(*self.SELECT_CITY).text
        assert 'Timisoara' in actual_value

    def tearDown(self) -> None:
        self.driver.quit()
