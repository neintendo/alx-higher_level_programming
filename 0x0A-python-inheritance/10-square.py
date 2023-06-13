#!/usr/bin/python3
"""
Module containing classes that define several shapes
and calculates areas
"""


class BaseGeometry:
    """
    Class containing an integer validator.
    """

    def integer_validator(self, name, value):
        """Validates value"""
        if isinstance(value, bool) == 1:
            raise TypeError("{:s} must be an integer".format(name))
        if isinstance(value, int) == 0:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class which defines a rectangle.
    """

    def __init__(self, width, height):
        """
        Sets values for Rectangle.

        Arguments:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.__width = width
        self.__height = height
        bg = BaseGeometry()
        bg.integer_validator("height", self.__height)
        bg.integer_validator("width", self.__width)

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of object Rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    A class which defines a square.
    """

    def __init__(self, size):
        """
        Sets values for Square.

        Arguments:
            size: the size of the square.
        """
        bg = BaseGeometry()
        bg.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """String representation of object Square"""
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))
