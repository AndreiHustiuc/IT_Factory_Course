from webdriver_manager.chrome import ChromeDriverManager

from src.API.OSM_api import get_map_data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

result = get_map_data('pub', '53.2987342,-6.3870259', '53.4105416,-6.1148829')
city = result['elements'][0]['tags']['addr:city']

driver = webdriver.Chrome(ChromeDriverManager().install())
link = 'https://www.openstreetmap.org/'
SEARCH_BAR = (By.CSS_SELECTOR, '#sidebar #query')
GO_BUTTON = (By.CSS_SELECTOR, "#sidebar .col .btn")
SELECT_CITY = (By.XPATH, '//a[@data-prefix="City"]')

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(link)
driver.find_element(*SEARCH_BAR).send_keys(city)
driver.find_element(*GO_BUTTON).click()
time.sleep(3)
# driver.find_element(*SELECT_CITY).click()
# time.sleep(3)
actual_value = driver.find_element(*SELECT_CITY).text
time.sleep(3)
# print(actual_value)
assert city in actual_value

driver.quit()

# todo: rezultatele salvate intr-un fisier json, apoi citim acel fisier si aplicam for loop pentru a extrage toate strazile, dupa ce avem strazile extrase integram cu selenium si verificam back-end cu front-end
