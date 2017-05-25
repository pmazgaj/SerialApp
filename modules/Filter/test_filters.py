"""
Unit tests for filters
"""
from unittest import TestCase

from SerialApp.modules.Filter.filter_new import FilterRawData, FilterScaleByMultiplier, FilterOverLimit, \
    FilterUnderLimit, FilterUniqueValues, MergeLists, FilterAverageValue

__author__ = "Przemek"


class TestingExamples:
    """"Only testing examples (test cases) for all child-filters (they inherit)"""
    data = [1, 2, 3, 4, 5]
    data_2 = [[1.1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], ]

    filter_raw_data = FilterRawData()

    filter_over_limit = FilterOverLimit(data_set=data, limit=3)
    filter_over_limit_data = filter_over_limit.data_set

    filter_scale_by_multiplier = FilterScaleByMultiplier(data_set=data, multiplier=5)
    filter_scale_by_multiplier_data = filter_scale_by_multiplier.data_set

    filter_under_limit = FilterUnderLimit(data_set=data, limit=2)
    filter_under_limit_data = filter_under_limit.data_set

    filter_unique_values = FilterUniqueValues(data_2)
    filter_unique_values_data = filter_unique_values.data_set

    filter_average_value_one = FilterAverageValue(data_set=data_2)
    filter_average_value_one_data = filter_average_value_one.data_set

    filter_average_value_two = FilterAverageValue(data_set=data_2)
    filter_average_value_two_data = filter_average_value_one.data_set

    merge_lists_one = MergeLists(data_2)
    merge_lists_one_data = merge_lists_one.data_set

    merge_lists_two = MergeLists(data)
    merge_lists_two_data = merge_lists_two.data_set


class TestFilterRawData(TestCase, TestingExamples):
    """Test raw data for filter (return of the original copy)"""
    def test_calculate(self):
        self.assertEqual(self.filter_raw_data.calculate(), [[4, 5, 6, 7, 8, 9, 10],
                                                       [14, 15, 6, 7, 8, 9, 1],
                                                       [4, 5, 12, 7, 8, 9, 12],
                                                       [4, 5, 6, 7, 8, 9, 10],
                                                       [24, 5, 12, 17, 8, 19, 100]])


class TestFilterScaleByMultiplier(TestCase, TestingExamples):
    """Tests for multiplying value (list) by given number"""
    def test_calculate(self):
        self.assertIsInstance(self.filter_scale_by_multiplier_data, list)
        self.assertEqual(self.filter_scale_by_multiplier_data, [5, 10, 15, 20, 25])


class TestFilterUnderLimit(TestCase, TestingExamples):
    """Tests for getting all values from (list) below parameter (number)"""
    def test_calculate(self):
        self.assertEqual(self.filter_under_limit_data, [1])


class TestFilterOverLimit(TestCase, TestingExamples):
    """Tests for getting all values from (list) over parameter (number)"""
    def test_calculate(self):
        self.assertListEqual(self.filter_over_limit_data, [4, 5])


class TestFilterUniqueValues(TestCase, TestingExamples):
    """Tests for getting all values from (list) that are distinct (unique)"""
    def test_calculate(self):
        self.assertEqual(self.filter_unique_values_data, [(1.1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)])
        self.assertIsInstance(self.filter_unique_values_data, list)


class TestFilterAverageValue(TestCase, TestingExamples):
    """Tests for getting lists of average values"""
    def test_calculate(self):
        self.assertEqual([], [])


class TestMergeLists(TestCase, TestingExamples):
    """Tests for list merging"""
    def test_calculate(self):
        self.assertEqual(self.merge_lists_one_data, [(1.1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)])
        self.assertIsInstance(self.merge_lists_two_data, list)
