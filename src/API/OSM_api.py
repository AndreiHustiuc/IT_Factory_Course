from pprint import pprint

import requests


def get_map_data(amenity, point_x, point_y):
    query = """
    [out:json];
    node
      [amenity=""" + amenity + """]
      (""" + point_x + """,""" + point_y + """);
    out;
    """
    url = 'https://overpass.kumi.systems/api/interpreter'
    response = requests.get(url=url, params={"data": query})
    return response.json()


if __name__ == '__main__':

    # print(response.json())
    result = get_map_data('pub', '53.2987342,-6.3870259', '53.4105416,-6.1148829')
    # pprint(result)
    # print(result['elements'][0]['tags']['website'])

    for key, value in result.items():
        if key == 'elements':
            for element in value:

                for key_tag, value_tag in element['tags'].items():
                    if key_tag == 'website':
                        print(value_tag)

# todo: creat fisiet json
