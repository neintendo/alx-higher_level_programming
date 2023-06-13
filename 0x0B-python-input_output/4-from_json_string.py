#!/usr/bin/python3
"""
Module containing a function to represent an object by a JSON string.
"""


def from_json_string(my_str):
    """
    Returns an object (Python Data Structure) represented by a JSON
    string.

    Arguments:
        my_str: the object to inspect.
    """
    import json
    return (json.loads(my_str))
