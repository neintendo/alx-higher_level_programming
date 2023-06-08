#!/usr/bin/python3
""" Creates an empty class Square that defines a square """


class Square:
    """
    Initialise with size without value checks.

    Arguments:
        __size: size of the square.

    Return: Nothing.
    """
    def __init__(self, __size=0):
        """Initialises the attribute size"""
        self.__size = __size
        pass
