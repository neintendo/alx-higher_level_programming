#!/usr/bin/python3
"""
This module provides a function that prints a square.

Usage:
    print_square = __import__('4-print_square').print_square
"""


def print_square(size):
    """
    Prints a square with the character "#"

    Args:
        size: the size of the square to print

    Return: nothing, just prints out a square to stdout
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int) and size < 0:
        raise TypeError("size must be an integer")

    for a in range(size):
        for b in range(size):
            print("#", end='')
        print()
