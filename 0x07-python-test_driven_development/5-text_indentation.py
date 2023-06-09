#!/usr/bin/python3
"""
This module provides a function that prints text with newlines
based on certain characters.

Usage:
    text_indentation = __import__('5-text_indentation').text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: the text to format
    Return: nothing, prints out formatted text.
    """
    space = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for a in text:
        if space == 1 and a != " ":
            space = 0
        if a == "." or a == "?" or a == ":":
            print("{:s}".format(a), end='')
            print(end="\n\n")
            space = 1
        else:
            if space != 1:
                print("{:s}".format(a), end='')
            space = 0
