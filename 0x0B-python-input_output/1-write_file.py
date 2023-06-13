#!/usr/bin/python3
"""
This module contains a function to write text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file in UTF-8.

    Arguments:
        filename: the file to write to.

    Return: the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
