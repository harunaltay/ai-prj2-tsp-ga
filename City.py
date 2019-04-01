import math


class City:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def measure_distance(self, city):
        delta_x = self.x - city.x
        delta_y = self.y - city.y
        distance = math.sqrt(delta_x**2 + delta_y**2)
        return distance

    def __str__(self):
        return self.index

    def __repr__(self):
        return self.index


