#!/usr/bin/python3
"""
Module containing a function which appends text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)

    Arguments:
        filename: the file to append to.

    Return: the number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
