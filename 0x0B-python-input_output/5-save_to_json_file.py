#!/usr/bin/python3
"""
Module containing a function that writes an object to a text
file using JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Arguments:
        my_obj: the object to write.
        filename: the file to write to.
    """
    import json

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
