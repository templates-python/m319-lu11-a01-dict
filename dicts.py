"""Exercises for working with Python dictionaries, using a dictionary of Swiss cities keyed by zip-code."""


def main():
    """
    Runs the dictionary exercises on a set of Swiss cities.
    """
    cities1 = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    add_cities(cities1)

    cities2 = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    remove_cities(cities2)

    cities3 = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    find_cities(cities3)
    loop_cities(cities3)
    sort_cities(cities3)


def add_cities(city_dict):
    """
    Adds two cities to the dictionary.

    :param city_dict (dict): dictionary of cities, keyed by zip-code
    :return: None
    """
    # TODO: add 2500 Biel
    # TODO: add 4000 Basel
    print('add_cities:\n', city_dict)


def remove_cities(dict_cities):
    """
    Removes a city from the dictionary.

    :param dict_cities (dict): dictionary of cities, keyed by zip-code
    :return: None
    """
    # TODO: remove the city with the zip-code 8400
    print('remove_cities:\n', dict_cities)


def find_cities(zip_city):
    """
    Finds cities in the dictionary by zip-code and by name.

    :param zip_city (dict): dictionary of cities, keyed by zip-code
    :return: None
    """
    print('find_city:')
    # TODO: print the name of the city with the zip-code 6000
    # TODO: print the zip-code of Genf
    pass


def loop_cities(city_dict):
    """
    Prints all cities using a loop.

    :param city_dict (dict): dictionary of cities, keyed by zip-code
    :return: None
    """
    print('loop_cities:')
    # TODO: print all cities in the list. output should be 'zip-code: name', i.e. '3000: Bern'


def sort_cities(dict_cities):
    """
    Sorts and prints the cities by zip-code.

    :param dict_cities (dict): dictionary of cities, keyed by zip-code
    :return: None
    """
    print('sort_cities:')
    # TODO: print all cities ordered by zip-Code (descending). output should be 'name: zip-code', i.e. 'Bern: 3000'


if __name__ == '__main__':
    main()
