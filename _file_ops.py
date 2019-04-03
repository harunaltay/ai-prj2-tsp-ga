from City import *


def cities_from_a_file(file_name):
    file = open(file_name, 'r+')
    lines = file.readlines()

    cities = []

    for line in lines:
        # print(line.strip())
        bir_line = line.strip()
        items = bir_line.split(" ")
        index = items[0]
        x = items[1]
        y = items[2]
        # print(index)
        # print(x)
        # print(y)
        # print()
        cities.append(City(index, x, y))

    return cities


def test_stub_cities_from_a_file():
    file_name = "data-cities/western-sahara.txt"
    cities = cities_from_a_file(file_name)
    for city in cities:
        print(city)


if __name__ == '__main__':
    test_stub_cities_from_a_file()

