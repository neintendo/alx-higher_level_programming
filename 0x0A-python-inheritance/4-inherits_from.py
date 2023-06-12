#!/bin/python3
"""
This module containts a function that checks the subclass
of an object.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a subclass of the
    specified class.

    Arguments:
        obj: the object to inspect.
        a_class: the class to check if obj is an instance of
                 a subclass.

    Return:
        True: if obj is a instance of a subclass.
        False: if obj is not an instance of a subclass.
    """

    if type(obj) != a_class:
        if issubclass(type(obj), a_class):
            return True
    else:
        return False
