from Route import *
import copy
import random


# a Population of Routes


class Population:
    def __init__(self, number_of_routes_in_population):
        self.routes = []
        self.number_of_routes_in_population = number_of_routes_in_population

    def sort_routes_by_fitness(self):
        self.routes = sorted(self.routes, reverse=True)

    def ctor_create_from_initial_cities(self, cities):
        for i in range(self.number_of_routes_in_population):
            route = Route(cities)
            route.shuffle()
            route.calculate_total_distance()
            route.calculate_fitness()
            self.routes.append(route)

    # tamamla
    def generate_the_next_population(self):
        child4, child5 = crossover_two_routes\
            (self.routes[0], self.routes[1], len(self.routes[0].cities))
        child6, child7 = crossover_two_routes\
            (self.routes[2], self.routes[3], len(self.routes[0].cities))

        child4.calculate_total_distance()
        child4.calculate_fitness()

        child5.calculate_total_distance()
        child5.calculate_fitness()

        child6.calculate_total_distance()
        child6.calculate_fitness()

        child7.calculate_total_distance()
        child7.calculate_fitness()

        self.routes[4] = child4
        self.routes[5] = child5
        self.routes[6] = child6
        self.routes[7] = child7

        for route in self.routes:
            r = random.random()
            if r <= 0.25:
                route.mutate()

    def to_string_fitness_and_total_distance(self):
        s = self.routes[0].to_string_fitness_and_total_distance()
        return s

