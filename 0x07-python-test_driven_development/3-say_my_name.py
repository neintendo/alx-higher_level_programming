#!/usr/bin/python3
"""
This module provides a function prints a name.

Usage:
    say_my_name = __import__('3-say_my_name').say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name with the format: My name is <first name> <last name>

    Args:
        first_name: First name
        last_name: Last name

    Return: nothing, just prints out to stdout.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
