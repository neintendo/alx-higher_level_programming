#!/usr/bin/python3
"""
This module provides a function that checks if an object is
kind of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the obj is kind of an instance of a_class.

    Arguments:
        obj: the object to inspect.
        a_class: the class to check if obj is an instance of.

    Return:
        True: if obj is an instance of a_class.
        False: if bj is not an instance of a_class.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
