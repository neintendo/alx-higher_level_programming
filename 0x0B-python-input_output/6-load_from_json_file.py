#!/usr/bin/python3
"""
Module which containts a function which creates an object
from a JSON file.
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Arguments:
        filename: the JSON file to create a object from.
    Return: the created object.
    """
    with open(filename, 'r+', encoding="utf-8") as file:
        import json
        return (json.load(file))
