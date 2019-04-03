"""
- a Route, starting in one of the cities, passing once every city,
returning to originating city.

- a candidate solution
- an individual solution
- a Kromozom
- a member in population
"""

import random
from random import randint
from City import *
from _file_ops import *


class Route:
    # file'den -> initial route oluşturulurken : shuffle yok
    # initial route'den -> population 0 oluşturulurken : shuffle var
    def __init__(self, cities):
        self.cities = cities
        self.fitness = 0.0
        self.total_distance = 0.0

    def mutate(self):
        # swap two cities

        a = randint(0, len(self.cities) - 1)
        b = randint(0, len(self.cities) - 1)

        city_a = self.cities[a].deep_copy()
        city_b = self.cities[b].deep_copy()

        self.cities[a] = city_b
        self.cities[b] = city_a

    def deep_copy(self):
        cities_copy = []
        for city in self.cities:
            cities_copy.append(city.deep_copy())
        route_copy = Route(cities_copy)
        route_copy.calculate_total_distance()
        route_copy.calculate_fitness()
        return route_copy

    def to_string_fitness_and_total_distance(self):
        s = str(self.total_distance) + ", " + str(self.fitness)
        return s

    def shuffle(self):
        random.shuffle(self.cities)

    def calculate_fitness(self):
        self.fitness = (1.0/self.total_distance) * 10000.0

    def calculate_total_distance(self):
        total_distance = 0.0
        number_of_cities = len(self.cities)
        for i in range(number_of_cities - 1):
            total_distance += self.cities[i].measure_distance(self.cities[i+1])
        total_distance += self.cities[0].measure_distance(self.cities[number_of_cities-1])
        self.total_distance = total_distance

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __ne__(self, other):
        return self.fitness != other.fitness

    def __repr__(self):
        return self.cities

    def __str__(self):
        s = ""
        for city in self.cities:
            s += str(city) + " "
        s = s.strip()
        return s


def crossover_two_routes(route1, route2, N):
    child_route_1 = route1.deep_copy()
    child_route_2 = route2.deep_copy()

    m = N//4
    print("m:", m)

    # TODO: burada bütün slice'ler aynı geliyor. düzeltmek lazım

    slice_11 = child_route_1.cities[:m]
    slice_12 = child_route_1.cities[m:]
    random.shuffle(slice_11)

    slice_21 = child_route_2.cities[:m]
    slice_22 = child_route_2.cities[m:]
    random.shuffle(slice_21)

    for slice in slice_21:
        slice_12.append(slice)

    for slice in slice_21:
        slice_22.append(slice)

    print("slice_12", str(slice_12))
    print("slice_22", str(slice_22))

    child_route_1.cities = slice_12
    child_route_2.cities = slice_22

    return child_route_1, child_route_2


def test_stub_initial_route_cities_from_a_file():
    file_name = "data-cities/western-sahara.txt"
    cities = cities_from_a_file(file_name)
    # for city in cities:
    #     print(city)

    initial_route = Route(cities)
    print(str(initial_route))

    initial_route.calculate_total_distance()
    initial_route.calculate_fitness()
    print("total_distance", initial_route.total_distance)
    print("fitness       ", initial_route.fitness)

    # initial_route.shuffle()


if __name__ == '__main__':
    test_stub_initial_route_cities_from_a_file()

