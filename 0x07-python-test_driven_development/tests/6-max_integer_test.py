#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_regular_input(self):
        """
        Test with a regular list of positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """
        Test with a list of negative integers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """
        Test with a list of mixed positive and negative integers.
        """
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        """
        Test with an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_all_equal_elements(self):
        """
        Test with a list where all elements are equal.
        """
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_float_numbers(self):
        """
        Test with a list of float numbers.
        """
        self.assertEqual(max_integer([2.5, 1.8, 3.7]), 3.7)

    def test_strings_in_list(self):
        """
        Test with a list containing a string.
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])

    def test_list_with_none(self):
        """
        Test with a list containing None.
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])


if __name__ == '__main__':
    unittest.main()
