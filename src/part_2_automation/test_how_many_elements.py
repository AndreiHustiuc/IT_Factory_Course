from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH_ELEMENT = 'Audi'
HOW_MANY_ELEMENTS = 10
AGREE_BUTTON = (By.ID, 'L2AGLb')
SEARCH_BOX = (By.NAME, 'q')
NEXT_PAGE = (By.ID, 'pnnext')
SEARCHED_ELEMENT = (By.XPATH, '//h3[@class = "LC20lb MBeuO DKV0Md"]')
DRIVER = webdriver.Chrome('..\\part_2_automation\\drivers\\chromedriver.exe')
LINK = 'https://www.google.com'


def setup(driver, link):
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(link)
    driver.find_element(*AGREE_BUTTON).click()
    driver.find_element(*SEARCH_BOX).send_keys(SEARCH_ELEMENT, Keys.RETURN)


def get_elements(driver):
    search_list = []
    while len(search_list) <= HOW_MANY_ELEMENTS:
        search_elements = driver.find_elements(*SEARCHED_ELEMENT)

        for element in search_elements:
            search_list.append(element.text)

        driver.find_element(*NEXT_PAGE).click()
        return search_list


def check_the_result(search_list):
    positive_result = 0
    negative_result = 0
    for item in search_list:

        if SEARCH_ELEMENT in item:
            positive_result += 1
        elif SEARCH_ELEMENT not in item:
            negative_result += 1

    print(f'There are {positive_result} results with {SEARCH_ELEMENT} and {negative_result} without {SEARCH_ELEMENT}')


def teardown(driver):
    driver.quit()


def main():
    setup(driver=DRIVER, link=LINK)
    my_list = get_elements(driver=DRIVER)
    check_the_result(search_list=my_list)
    teardown(driver=DRIVER)


if __name__ == '__main__':
    main()
