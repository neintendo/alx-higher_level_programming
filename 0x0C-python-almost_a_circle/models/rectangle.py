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
                if argt == 0:
                    self.__id = args[0]
                if argt == 1:
                    self.__width = args[1]
                if argt == 2:
                    self.__height = args[2]
                if argt == 3:
                    self.__x = args[3]
                if argt == 4:
                    self.__y = args[4]
        else:
            for n, v in kwargs.items():
                if n == "id":
                    self.__id = v
                elif n == "width":
                    self.__width = v
                elif n == "height":
                    self.__height = v
                elif n == "x":
                    self.__x = v
                elif n == "height":
                    self.__y = v
                else:
                    pass

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
        if isinstance(value, int) != 1:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if isinstance(value, int) != 1:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if isinstance(value, int) != 1:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
