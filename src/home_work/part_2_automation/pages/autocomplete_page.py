from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class Autocomplete(BasePage):
    ADDRESS_ID = 'autocomplete'
    STREET_NUMBER_ID = 'street_number'
    STREET_NUMBER_2_ID = 'route'
    CITY_ID = 'locality'
    STATE_ID = 'administrative_area_level_1'
    ZIP_CODE_ID = 'postal_code'
    COUNTRY_ID = 'country'

    def enter_address_name(self, address):
        self._driver.find_element(By.ID, self.ADDRESS_ID).send_keys(address)

    def enter_street_address_name(self, street_number):
        self._driver.find_element(By.ID, self.STREET_NUMBER_ID).send_keys(street_number)

    def enter_street_address_2(self, value):
        self._driver.find_element(By.ID, self.STREET_NUMBER_2_ID).send_keys(value)

    def enter_city(self, value):
        self._driver.find_element(By.ID, self.CITY_ID).send_keys(value)

    def enter_state(self, value):
        self._driver.find_element(By.ID, self.STATE_ID).send_keys(value)

    def enter_zip_code(self, value):
        self._driver.find_element(By.ID, self.ZIP_CODE_ID).send_keys(value)

    def enter_country(self, value):
        self._driver.find_element(By.ID, self.COUNTRY_ID).send_keys(value)
