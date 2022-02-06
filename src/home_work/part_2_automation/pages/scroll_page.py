from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage
from datetime import datetime


class Scroll(BasePage):
    DATE = datetime.now().strftime('%m/%d/%Y')

    def scroll_page(self):
        self._driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self._driver.find_element(By.ID, 'name').send_keys('Nume Prenume')
        self._driver.find_element(By.ID, 'date').send_keys(self.DATE)
