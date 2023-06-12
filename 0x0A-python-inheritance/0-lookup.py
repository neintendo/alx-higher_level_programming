#!/usr/bin/python3
"""
This module provides a function to retrieve a list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Get a list of available attributes and methods of an object.

    Arguments:
        obj: the object to inspect.

    Return: List of available attributes and methods of an object.
    """
    return (dir(obj))
