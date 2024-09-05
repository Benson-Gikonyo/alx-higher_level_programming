#!/usr/bin/python3
"""unit test for def max_integer(list=[])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntergerTest(unittest.TestCase):
    """test functions for max_interger function"""
    
    def test_max_integer(self):
        """tests successful cases of max_integer"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 1, 3, 3, 3, 6, 8, 8]), 8)
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)

    def test_empty(self):
        """tests argument is none error"""
        self.assertIsNone(max_integer())

    def test_errors(self):
       """tests incorrect type argument errors"""
       self.assertRaises(Exception, max_integer, ["string", 1.73, 25, {2}])
