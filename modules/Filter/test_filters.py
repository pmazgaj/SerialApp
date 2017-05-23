"""
Unit tests for filters
"""
from unittest import TestCase

from SerialApp.modules.Filter.filter_new import FilterRawData, FilterScaleByMultiplier, FilterOverLimit, \
    FilterUnderLimit, FilterUniqueValues

__author__ = "Przemek"

data = [1, 2, 3, 4, 5]
data_2 = [[1.1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], ]

filter_raw_data = FilterRawData()
filter_over_limit = FilterOverLimit(data_set=data, limit=3)
filter_scale_by_multiplier = FilterScaleByMultiplier(data_set=data, multiplier=5)
print(filter_scale_by_multiplier)
filter_under_limit = FilterUnderLimit(filter_scale_by_multiplier.data_set, limit=24)
filter_unique_values = FilterUniqueValues(data_2)


class TestFilterRawData(TestCase):
    def test_calculate(self):
        # self.assertEqual(filter_raw_data.calculate(), data)
        pass


class TestFilterScaleByMultiplier(TestCase):
    def test_calculate(self):
        self.assertIsInstance(filter_scale_by_multiplier.data_set, list)
        self.assertEqual(filter_scale_by_multiplier.data_set, [5, 10, 15, 20, 25])


class TestFilterUnderLimit(TestCase):
    def test_calculate(self):
        # self.fail()
        pass


class TestFilterOverLimit(TestCase):
    def test_calculate(self):
        # self.fail()
        pass


class TestFilterUniqueValues(TestCase):
    def test_calculate(self):
        # self.fail()
        pass
