#!/usr/bin/python3
"""
Module that contains 2 classes which is still in progress
but is starting to make sense :)
"""


class BaseGeometry:
    """
    Still in progress :)
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
    A class rectangle which instantiates with width & height.
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
