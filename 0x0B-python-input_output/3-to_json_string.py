#!/usr/bin/python3
"""
Module containing a function to view the JSON representation.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Arguments:
        my_obj: the object to inspect.
    """
    import json
    return (json.dumps(my_obj))
