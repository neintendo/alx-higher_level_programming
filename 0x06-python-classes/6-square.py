#!/usr/bin/python3
""" Creates an empty class Square that defines a square """


class Square:
    """
    Initialise with size with value checks.

    Arguments:
        __size: size of the square.

    Return: Nothing.
    """

    def __init__(self, __size=0, __position=(0, 0)):
        """Initialises the attribute size"""
        self.__size = __size
        self.__position = __position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in STDOUT the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
