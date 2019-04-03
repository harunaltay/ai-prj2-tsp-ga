from Population import *
from _file_ops import *

number_of_iterations = 10
number_of_routes_in_population = 8  # Population size

file_name = "data-cities/western-sahara.txt"
cities = cities_from_a_file(file_name)

#  create route_initial --------------------------------------------------

route_initial = Route(cities)
route_initial.shuffle()
print(str(route_initial))

route_initial.calculate_total_distance()
route_initial.calculate_fitness()
print("total_distance", route_initial.total_distance)
print("fitness       ", route_initial.fitness)

result_first = "first result: " + \
               str(route_initial.total_distance) + ", " + str(route_initial.fitness)

#  create Population 0 --------------------------------------------------

population_initial = Population(number_of_routes_in_population)
population_initial.ctor_create_from_initial_cities(cities)  # 8 tane shuffle ile
population_initial.sort_routes_by_fitness()

generation_number = 0

print("population/generation:", generation_number)
print(population_initial.to_string_fitness_and_total_distance())
i = 1
for route in population_initial.routes:
    print(i, route.total_distance, route.fitness)
    i += 1

print()

population = population_initial

#  create Population 1 to number_of_iterations --------------------------------------------------

for i in range(number_of_iterations):
    population.generate_the_next_population()
    population.sort_routes_by_fitness()

    generation_number += 1
    print("population/generation:", generation_number)
    print(population.to_string_fitness_and_total_distance())
    print()

print("-----------------------------")
print()

result_last = "last result:  " + \
               population.to_string_fitness_and_total_distance()

print(result_first)
print(result_last)

