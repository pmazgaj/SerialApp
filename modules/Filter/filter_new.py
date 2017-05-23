"""
Handle behaviour of data filters
"""
from abc import ABC, abstractmethod

__author__ = "Przemek"


class Filter(ABC):
    """Base class for filter (define parameters for them)"""
    DATA_ORIGINAL = [[4, 5, 6, 7, 8, 9, 10],
                     [14, 15, 6, 7, 8, 9, 1],
                     [4, 5, 12, 7, 8, 9, 12],
                     [4, 5, 6, 7, 8, 9, 10],
                     [24, 5, 12, 17, 8, 19, 100]]

    @abstractmethod
    def __init__(self):
        self.data_set = None
        self.multiplier = 1

    @abstractmethod
    def calculate(self):
        raise NotImplementedError

    def __str__(self):
        return '{}'.format(self.data_set)


class FilterUniqueValues(Filter):
    """Filter values, that have occured before"""

    def __init__(self, data_set: list = ()):
        super(FilterUniqueValues, self).__init__()
        self.data_set = data_set
        self.calculate()

    def calculate(self):
        return [x for x in self.data_set if x not in self.data_set]
        unique_list = []
        data = self.DATA_ORIGINAL
        # print(data)
        # print(data.__class__)
        # choice = [element for i in range(len(data)) for element in data[i]]
        # print(len(choice))

        for index, value in enumerate(data):
            for i, elem in enumerate(value):

                if index > 0:
                    if i == value[index - 1][i]:
                        print(elem)
                    unique_list.append(value[i])
                    print(data[index - 1])
                    # zipped = [x + y for x, y in zip(value, List2)]
                    # unique_list.append(zipped)
        # print(zipped)
        print(unique_list)
        for index, value in enumerate(data):
            unique_list = [x for index_elem, x in enumerate(value)]
            # print(unique)

            if index > 0:
                ...
                # print(value)
                # print(index)
                # unique = [[] for x in enumerate(range(len(value)))]
                # non_unique = [[] for x in enumerate(range(len(value)))]
                # for i, element in enumerate(value):
                #     unique[i].append([element])
                # print(unique)
                # non_unique = [[] for x in range(len(value))]
                # print(unique)
                # print(non_unique)
                # for index_elem, element in enumerate(value):
                # unique[index_elem].append(element)
                # if index > 0:
                #     a = value[index_elem]
                #     b = data[index - 1][index_elem]
                #     print('a: {} b: {} a==b{}'.format(a, b, a==b))
                #
                #     if value[index_elem] != data[index - 1][index_elem]:
                #         unique[index_elem].append(element)
                # print(element)
                # a = unique[index_elem]
                # print((a.__class__))
                # unique[index_elem].append(elem)
                # print(unique)
                # if index > 0:
                #     if value[index_elem] != data[index][index_elem - 1]:
                #         unique[index_elem].append(elem)
                #         print(elem)
                # ...
                # if index_elem == len(value) - 1:
                #     ...
                # print('\n')
                # print(unique)

    def __str__(self):
        return '{}'.format(self.data_set)


class FilterRawData(Filter):
    """Filter values, that have occured before"""

    def __init__(self, data_set: list = ()):
        super(FilterRawData, self).__init__()
        self.data_set = data_set
        self.data_set = self.calculate()

    def calculate(self):
        """return not formatted data"""
        return self.DATA_ORIGINAL


class FilterScaleByMultiplier(Filter):
    """Multiply values by given multiplier"""

    def __init__(self, data_set: list = (), multiplier: int = 1):
        super(FilterScaleByMultiplier, self).__init__()
        self.data_set = data_set
        self.multiplier = multiplier
        self.data_set = self.calculate()

    def calculate(self):
        return [elem * self.multiplier for elem in self.data_set]


class FilterUnderLimit(Filter):
    """Filter values by given limit (up to this limit)"""

    def __init__(self, data_set: list = (), multiplier: int = 1, limit: int = 100):
        super(FilterUnderLimit, self).__init__()
        self.data_set = data_set
        self.multiplier = multiplier
        self.limit = limit
        self.data_set = self.calculate()

    def calculate(self):
        return [elem for elem in self.data_set if elem < self.limit]


class FilterOverLimit(Filter):
    """Filter values by given limit (over the limit)"""

    def __init__(self, data_set: list = (), multiplier: int = 1, limit: int = 100):
        super(FilterOverLimit, self).__init__()
        self.data_set = data_set
        self.multiplier = multiplier
        self.limit = limit
        self.data_set = self.calculate()

    def calculate(self):
        return [elem for elem in self.data_set if elem > self.limit]

data = [1, 2, 3, 4, 5]

b = FilterOverLimit(data_set=data, limit=3)
c = FilterScaleByMultiplier(b.data_set, multiplier=5)
d = FilterUnderLimit(c.data_set, limit=24)
e = FilterUniqueValues(d.data_set, limit=24)
print(b)
print(c)
print(d)
data = FilterRawData()
print(data)
# a = FilterUniqueValues()
# b = FilterScaleByMultiplier()
# print(b)
