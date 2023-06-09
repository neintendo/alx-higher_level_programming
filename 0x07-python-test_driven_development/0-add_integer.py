#!/usr/bin/python3
"""
This module provides a function that adds two integers,

Usage: add_integer = __import__('0-add_integer').add_integer
"""


def add_integer(a, b=98):
    """
    Return: the sum of a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return (a + b)
