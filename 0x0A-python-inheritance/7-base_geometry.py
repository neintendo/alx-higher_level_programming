#!/usr/bin/python3
"""
Module that contains BaseGeometry which is still in progress
but is starting to make sense :)
"""


class BaseGeometry:
    """
    Still in progress :)
    """

    def area(self):
        """Raises an exception to indicate an unimplemented function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if isinstance(value, int) == 0:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
