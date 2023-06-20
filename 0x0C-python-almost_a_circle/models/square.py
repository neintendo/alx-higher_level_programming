#!/usr/bin/python3
"""
This module contains a class which defines a Rectangle
and several functions within the class that allow it to be
displayed to STDOUT.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square with width and height attributes.
    x and y are for STDOUT spacing.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of object Square"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if len(args) != 0:
            for argt in range(len(args)):
                attributes = ["id", "size", "x", "y"]
                for i, value in enumerate(args):
                    if i < len(attributes):
                        setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Square."""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
