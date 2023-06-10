#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_MaxInteger(__self):
        __self.assertEqual(max_integer([1, 3, 20]), 20)
        __self.assertEqual(max_integer([1, 20, 3]), 20)
        __self.assertEqual(max_integer([20, 3, 1]), 20)
        __self.assertEqual(max_integer([1, 3, -20]), 3)
        __self.assertEqual(max_integer([2]), 2)
        __self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_None(__self):
        __self.assertIsNone(max_integer([]), None)

    def test_Instance(__self):
        __self.assertRaises(TypeError, max_integer("eh"))


if __name__ == "__main__":
    unittest.main()
