"""
Create random data for an application, in similar pattern to serial data
"""
import random

__author__ = "Przemek"


class RandomDataHandler:
    def __init__(self):
        ...

    def get_random_num_in_range(self, range_of_data: list) -> float:
        """get random float number in given range, for 3 decimal places """
        number = random.uniform(range_of_data[0], range_of_data[1])
        return round(number, 3)

    def create_random_data(self, tuple_with_ranges: list) -> list:
        """creates random data for an application"""
        while True:
            return [self.get_random_num_in_range(range_num) for range_num in tuple_with_ranges]


a = RandomDataHandler()

for x in range(0, 1000):
    a.create_random_data([(0, 22), (3, 14), [99, 228]])

    print(a.create_random_data([(0, 22), (3, 14), [99, 228]]))
