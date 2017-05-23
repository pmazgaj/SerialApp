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


class FilterUniqueValues(Filter):
    """Filter values, that have occured before"""

    def __init__(self, data_set: list = ()):
        super(FilterUniqueValues, self).__init__()
        self.data_set = data_set
        self.data_set = self.calculate()

    def calculate(self):
        data_set = list(zip(*self.data_set))
        return data_set

    def __str__(self):
        return '{}'.format(self.data_set)
