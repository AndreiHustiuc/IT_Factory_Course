from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import Select

DRIVER = webdriver.Chrome(executable_path='..\\part_2_automation\\drivers\\chromedriver.exe')
LINK = 'https://www.openstreetmap.org/'
CITIES = ['Bucuresti', 'Cluj-Napoca', 'Bistrita', 'Sibiu', 'Ploiesti', 'Bacau', 'Suceava', 'Galati', 'Arad',
          'Timisoara']
SEARCH_BAR = (By.CSS_SELECTOR, '#sidebar #query')
GO_BUTTON = (By.CSS_SELECTOR, "#sidebar .col .btn")
GO_ROUTE = (By.CSS_SELECTOR, "#sidebar .routing_go")
SELECT_CITY = (By.XPATH, '//a[@data-prefix="City"]')
DIRECTION_BUTTON = (
    By.CSS_SELECTOR, '#sidebar > div.search_forms > form.search_form.px-1.py-2 > div > div.col-auto > a')
FROM = (By.CSS_SELECTOR, '#sidebar #route_from')
TO = (By.CSS_SELECTOR, '#sidebar #route_to')
ROUTING_ENGINES = (By.CSS_SELECTOR,
                   '#sidebar > div.search_forms > form.directions_form.pb-3 > div:nth-child(4) > div.col.offset-1 > select')
ROUTE = (By.XPATH, '//td[@class="instruction"]')


def setup(driver, link):
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(link)


def find_one_city(driver, city):
    driver.find_element(*SEARCH_BAR).send_keys(city)
    driver.find_element(*GO_BUTTON).click()
    time.sleep(3)
    actual_value = driver.find_element(*SELECT_CITY).text

    assert 'Timișoara' in actual_value


def find_multiple_cities(driver, city_list):
    for city in city_list:
        driver.find_element(*SEARCH_BAR).send_keys(city)
        driver.find_element(*GO_BUTTON).click()
        time.sleep(3)
        driver.find_element(*SELECT_CITY).click()


def get_a_route(driver, city_list):
    driver.find_element(*DIRECTION_BUTTON).click()
    time.sleep(2)
    driver.find_element(*FROM).send_keys(random.choice(city_list))
    driver.find_element(*TO).send_keys(random.choice(city_list))
    driver.find_element(*GO_ROUTE).click()


def get_a_route_with(driver, city_list):
    driver.find_element(*DIRECTION_BUTTON).click()
    time.sleep(2)
    driver.find_element(*FROM).send_keys(random.choice(city_list))
    driver.find_element(*TO).send_keys(random.choice(city_list))
    time.sleep(2)
    select = Select(driver.find_element(*ROUTING_ENGINES))
    for i in range(6):
        select.select_by_value(str(i))
        time.sleep(3)


def route_on_bike(driver, city_list):
    driver.find_element(*DIRECTION_BUTTON).click()
    time.sleep(2)
    driver.find_element(*FROM).send_keys(random.choice(city_list))
    driver.find_element(*TO).send_keys(random.choice(city_list))
    time.sleep(2)
    select = Select(driver.find_element(*ROUTING_ENGINES))
    select.select_by_value('1')
    route = driver.find_elements(*ROUTE)
    # print(f'How many items in route list: {len(route)}')

    index = 1
    while index <= len(route):
        driver.find_element(By.XPATH, f'//td[@class="instruction"]//b[text()="{str(index) + "."}"]').click()
        time.sleep(0.5)
        index = index + 1


def distance_between_two_points(driver, city_list):
    driver.find_element(*DIRECTION_BUTTON).click()
    time.sleep(2)

    route_dict = dict()

    while len(route_dict) < 2:
        from_city = random.choice(city_list)
        to_city = random.choice(city_list)
        if from_city == to_city:
            to_city = random.choice(city_list)

        driver.find_element(*FROM).send_keys(from_city)
        time.sleep(1)
        driver.find_element(*TO).send_keys(to_city)
        time.sleep(1)
        driver.find_element(*GO_ROUTE).click()
        time.sleep(5)

        # get distance and time
        distance_time = driver.find_element(By.XPATH, '//*[@id="sidebar_content"]/p[1]').text

        items = [item[:-1] for item in distance_time.split(' ')]
        route_distance = items[1]
        route_time = items[3]

        route_dict.update({f'from {from_city} to {to_city}': {'Distance': route_distance, 'Time': route_time}})

        driver.find_element(*FROM).clear()
        time.sleep(1)
        driver.find_element(*TO).clear()
        time.sleep(1)

    dest, dist = list(), list()

    for cities in route_dict.items():
        dest.append(cities[0])
        dist.append(cities[1]["Distance"][:-2])

    if dist[0] > dist[1]:
        print(
            f'Route {dest[0]} = {dist[0]}km, is longer than {dest[1]} = {dist[1]}km with {int(dist[0]) - int(dist[1])}km')
    else:
        print(
            f'Route {dest[1]} = {dist[1]}km, is longer than {dest[0]} = {dist[0]}km with {int(dist[1]) - int(dist[0])}km')


def zoom(driver, zoom_scale):
    time.sleep(2)
    actual_zoom = int(driver.find_element(By.XPATH, '//*[@id="map"]/div[2]/div[3]/div/div[1]').text[:-3])
    zoom_in = driver.find_element(By.XPATH, '//*[@id="map"]/div[2]/div[2]/div[1]/a[1]/span')
    zoom_out = driver.find_element(By.XPATH, '//*[@id="map"]/div[2]/div[2]/div[1]/a[2]/span')

    if actual_zoom > zoom_scale:
        while actual_zoom > zoom_scale:
            zoom_in.click()
            time.sleep(3)
            actual_zoom = int(driver.find_element(By.XPATH, '//*[@id="map"]/div[2]/div[3]/div/div[1]').text[:-3])

    elif actual_zoom < zoom_scale:
        while actual_zoom < zoom_scale:
            zoom_out.click()
            time.sleep(3)
            actual_zoom = int(driver.find_element(By.XPATH, '//*[@id="map"]/div[2]/div[3]/div/div[1]').text[:-3])


def teardown(driver):
    time.sleep(3)
    driver.quit()


def main():
    setup(driver=DRIVER, link=LINK)
    find_one_city(driver=DRIVER, city='Timisoara')
    # find_multiple_cities(driver=DRIVER, city_list=CITIES)
    # get_a_route(driver=DRIVER, city_list=CITIES)
    # get_a_route_with(driver=DRIVER, city_list=CITIES)
    # route_on_bike(driver=DRIVER, city_list=CITIES)
    # distance_between_two_points(driver=DRIVER, city_list=CITIES)
    # zoom(driver=DRIVER, zoom_scale=250)
    teardown(driver=DRIVER)


if __name__ == '__main__':
    main()
