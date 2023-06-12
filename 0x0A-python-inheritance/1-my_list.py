#!/usr/bin/python3
"""
This module provides a function to print a sorted list without modifying
the original one.
"""


class MyList(list):
    """
    A custom list class that extends the functionality of the built-in
    list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        This method creates a sorted copy of the list and prints it.
        The original list remains unchanged.
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print("{:}".format(sorted_list))
