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
        self.__size = __size

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int) != 1:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints in STDOUT the square with the character #"""
        if self.__size == 0:
            print()
        for a in range(self.__size):
            for b in range(self.__size):
                print("#", end='')
            print()
