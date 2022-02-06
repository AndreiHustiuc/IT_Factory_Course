from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class HomePage(BasePage):
    AUTOCOMPLETE = (By.LINK_TEXT, 'Autocomplete')
    BUTTONS = 'Buttons'
    CHECKBOX = 'Checkbox'
    DATEPICKER = 'Datepicker'
    DRAG_DROP = 'Drag and Drop'
    DROP_DOWN = 'Dropdown'
    ENABLED_DISABLED = 'Enabled and disabled elements'
    FILE_UPLOAD = 'File Upload'
    KEY_MOUSE_PRESS = 'Key and Mouse Press'
    MODAL = 'Modal'
    PAGE_SCROLL = 'Page Scroll'
    RADIO_BUTTON = 'Radio Button'
    SWITCH_WINDOW = 'Switch Window'
    WEB_FORM = 'Complete Web Form'

    def go_to_autocomplete(self):
        self._driver.find_element(*self.AUTOCOMPLETE).click()

    def go_to_buttons(self):
        self._driver.find_element(By.LINK_TEXT, self.BUTTONS).click()

    def go_to_checkbox(self):
        self._driver.find_element(By.LINK_TEXT, self.CHECKBOX).click()

    def go_to_datepicker(self):
        self._driver.find_element(By.LINK_TEXT, self.DATEPICKER).click()

    def go_to_drag_and_drop(self):
        self._driver.find_element(By.LINK_TEXT, self.DRAG_DROP).click()

    def go_to_dropdown(self):
        self._driver.find_element(By.LINK_TEXT, self.DROP_DOWN).click()

    def go_to_enb_and_disab_elem(self):
        self._driver.find_element(By.LINK_TEXT, self.ENABLED_DISABLED).click()

    def go_to_file_upload(self):
        self._driver.find_element(By.LINK_TEXT, self.FILE_UPLOAD).click()

    def go_to_key_and_mouse_press(self):
        self._driver.find_element(By.LINK_TEXT, self.KEY_MOUSE_PRESS).click()

    def go_to_modal(self):
        self._driver.find_element(By.LINK_TEXT, self.MODAL).click()

    def go_to_page_scroll(self):
        self._driver.find_element(By.LINK_TEXT, self.PAGE_SCROLL).click()

    def go_to_radio_button(self):
        self._driver.find_element(By.LINK_TEXT, self.RADIO_BUTTON).click()

    def go_to_switch_window(self):
        self._driver.find_element(By.LINK_TEXT, self.SWITCH_WINDOW).click()

    def go_to_complete_web_form(self):
        self._driver.find_element(By.LINK_TEXT, self.WEB_FORM).click()
