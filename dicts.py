def main():
    """
    main program - creates some dictionaries and calls the functions
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
    adds two cities
    :param city_dict: dictionary of cities
    :return: None
    """
    # TODO: add 2500 Biel
    # TODO: add 4000 Basel
    print('add_cities:\n', city_dict)

def remove_cities(dict_cities):
    """
    removes a city
    :param dict_cities: dictionary of cities
    :return: None
    """
    # TODO: remove the city with the zip-code 8400
    print('remove_cities:\n', dict_cities)


def find_cities(zip_city):
    """
    finds a city
    :param zip_city: dictionary of cities
    :return: None
    """
    print('find_city:')
    # TODO: print the name of the city with the zip-code 6000
    # TODO: print the zip-code of Genf
    pass


def loop_cities(city_dict):
    """
    prints all cities using a loop
    :param city_dict: dictionary of cities
    :return: None
    """
    print('loop_cities:')
    # TODO: print all cities in the list. output should be 'zip-code: name', i.e. '3000: Bern'


def sort_cities(dict_cities):
    """
    sorts the cities by zip-code
    :param dict_cities: dictionary of cities
    :return: None
    """
    print('sort_cities:')
    # TODO: print all cities ordered by zip-Code (descending). output should be 'name: zip-code', i.e. 'Bern: 3000'

if __name__ == '__main__':
    main()