#!/usr/bin/python3
"""
This module contains a class which defines a Rectangle
and several functions within the class that allow it to be
displayed to STDOUT.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with width and height attributes.
    x and y are for STDOUT spacing.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructs a rectangle with the specified arguments.

        Arguments:
            width: the width of the rectangle.
            height: the height of the rectangle.
            x: horizontal spacing.
            y: vertical spacing.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = super().__init__(id)

    def validation(self, name, value):
        """Validates dimension values"""
        if isinstance(value, int) is not True:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0:
            if name == "x" or name == "y":
                raise ValueError("{:s} must be >= 0".format(name))
        if value <= 0:
            raise ValueError("{:s} must be > 0".format(name))

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance using the character #"""
        for ry in range(self.__y):
            print(" ")
        for a in range(self.__height):
            for rx in range(self.__x):
                print(" ", end='')
            for b in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """String representation of object Rectangle"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                (self.__id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if len(args) != 0:
            for argt in range(len(args)):
                attributes = ["id", "width", "height", "x", "y"]
                for i, value in enumerate(args):
                    if i == 0:
                        self.__id = value
                    if i < len(attributes):
                        setattr(self, attributes[i], value)
        else:
            if "id" in kwargs:
                self.__id = kwargs["id"]
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.validation("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.validation("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value
