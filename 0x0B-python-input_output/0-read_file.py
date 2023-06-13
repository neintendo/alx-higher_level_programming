#!/usr/bin/python3
"""
This module contains a function with reads a file and
prints it to STDOUT.
"""


def read_file(filename=""):
    """
    Reads a text file in UTF-8 and prints it to STDOUT.

    Arguments:
        filename: the file to read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
