from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import pyautogui


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://formy-project.herokuapp.com/fileupload')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, ).click()
pyautogui.write('C:\\Users\\Moldoveanu\\Desktop\\New Text Document.txt', interval=0.1)
pyautogui.press('return')

time.sleep(5)
driver.quit()