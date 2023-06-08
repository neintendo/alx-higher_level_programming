#!/usr/bin/python3
""" Creates an empty class Square that defines a square """


class Square:
    """
    Initialise with size with value checks.

    Arguments:
        __size: size of the square.

    Return: Nothing.
    """

    def __init__(self, __size=0):
        """Initialises the attribute size"""
        if isinstance(__size, int) == 0:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
