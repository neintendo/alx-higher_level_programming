#!/usr/bin/python3
"""
Module containing a base class for other classes in the project.
"""


class Base:
    """
    This is the base class for all the other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises public instance attribute id"""
        if id is not None:
            self.id = id
            return (self.id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            return (self.id)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Arguments:
            list_dictionaries: is a list of dictionaries.
        """
        import json

        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
