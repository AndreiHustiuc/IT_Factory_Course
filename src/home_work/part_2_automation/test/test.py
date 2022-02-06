import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.home_work.part_2_automation.pages.button_page import Button
from src.home_work.part_2_automation.pages.checkbox_page import CheckBox
from src.home_work.part_2_automation.pages.datepicker_page import DatePicker
from src.home_work.part_2_automation.pages.drag_drop_page import DragAndDrop
from src.home_work.part_2_automation.pages.drop_down_page import DropDown
from src.home_work.part_2_automation.pages.enables_disabled_page import EnabledDisabled
from src.home_work.part_2_automation.pages.file_upload_page import FileUpload
from src.home_work.part_2_automation.pages.home_page import HomePage
from src.home_work.part_2_automation.pages.scroll_page import Scroll


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self._driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_1(self):
        self._driver.get('https://formy-project.herokuapp.com/')
        main_page = HomePage(self._driver)
        return main_page

    def test_drag_and_drop(self):
        self._driver.get('https://formy-project.herokuapp.com/dragdrop')
        test = DragAndDrop(self._driver)
        test.drag_and_drop()

    def test_input_text(self):
        main_page = self.test_1()
        main_page.go_to_enb_and_disab_elem()
        test = EnabledDisabled(self._driver)
        test.enter_text('this is enabled text box')

    def test_upload_file(self):
        main_page = self.test_1()
        main_page.go_to_file_upload()
        test = FileUpload(self._driver)
        test.upload_file("C:\\Users\\Moldoveanu\\Pictures\\ASUS.png")
        time.sleep(5)
        test.upload_reset()

    def test_scroll_page(self):
        main_page = self.test_1()
        main_page.go_to_page_scroll()
        test = Scroll(self._driver)
        test.scroll_page()

    def tearDown(self) -> None:
        time.sleep(2)
        self._driver.quit()
