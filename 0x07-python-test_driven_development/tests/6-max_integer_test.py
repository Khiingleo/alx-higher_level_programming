#!/usr/bin/python3
"""Unitest for max_integer([...])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        """test with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_integers(self):
        """test with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        """test with mixed integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-4, 3, -2, 1]), 3)

    def test_duplicate_integers(self):
        """test with duplicate integers"""
        self.assertEqual(max_integer([1, 2, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_string(self):
        """test with string"""
        self.assertEqual(max_integer("creamer"), "r")

    def test_floats(self):
        """test with floats"""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.9]), 15.2)

    def test_string_list(self):
        """ test with string list"""
        lists = ["John", "is", "my", "name"]
        self.assertEqual(max_integer(lists), "name")


if __name__ == '__main__':
    unittest.main()
