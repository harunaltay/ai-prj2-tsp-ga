"""
- a Route, starting in one of the cities, passing once every city,
returning to originating city.

- a candidate solution
- an individual solution
- a Kromozom
- a member in population
"""

import random


class Route:
    def __init__(self, cities):
        self.cities = cities
        random.shuffle(self.cities)  # !!!
        self.fitness = 0.0
        self.is_fitness_changed = True

    def calculate_total_distance(self):
        total_distance = 0.0
        number_of_cities = len(self.cities)
        for i in range(number_of_cities - 1):
            total_distance += self.cities[i].measure_distance(self.cities[i+1])
        total_distance += self.cities[0].measure_distance(self.cities[-1])
        return total_distance

    def get_fitness(self):
        if self.is_fitness_changed == True:
            self.fitness = (1/self.calculate_total_distance()) * 10000
            self.is_fitness_changed = False
        return self.fitness

    def get_cities(self):
        self.is_fitness_changed = True
        return self.cities

    def __repr__(self):
        return self.cities

    def __str__(self):
        s = ""
        for city in self.cities:
            s += city + " "
        s = s.strip()
        return s

