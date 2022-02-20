import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.CLASS_NAME, 'radius')
    MESSAGE = (By.ID, 'flash')
    SUB_HEADER = (By.CLASS_NAME, 'subheader')
    LOGOUT = (By.CSS_SELECTOR, '#content > div > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='..\\part_2_automation\\drivers\\chromedriver.exe')
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_empty_space(self):
        self.driver.find_element(*self.USERNAME).send_keys('')
        self.driver.find_element(*self.PASSWORD).send_keys('')
        self.driver.find_element(*self.LOGIN).click()
        actual_message = self.driver.find_element(*self.MESSAGE).text
        assert 'invalid' in actual_message

    def test_invalid_user_password(self):
        self.driver.find_element(*self.USERNAME).send_keys('username')
        self.driver.find_element(*self.PASSWORD).send_keys('password')
        self.driver.find_element(*self.LOGIN).click()
        actual_message = self.driver.find_element(*self.MESSAGE).text
        assert 'invalid' in actual_message

    def test_valid_username_password(self):
        user_pass = self.driver.find_elements(By.XPATH, '//h4[@class="subheader"]//em')
        user = user_pass[0].text
        pwd = user_pass[1].text

        self.driver.find_element(*self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.LOGIN).click()
        actual_message = self.driver.find_element(*self.MESSAGE).text
        assert 'logged' in actual_message

    def tearDown(self) -> None:
        self.driver.quit()
