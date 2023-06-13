#!/usr/bin/python3
"""
This module contains a class which inverses certain operators.
"""


class MyInt(int):
    """
    A rebel which has == and != operators inverted.
    """

    def __eq__(self, integer):
        """Override == operator"""
        return super().__ne__(integer)

    def __ne__(self, integer):
        """Override != operator"""
        return super().__eq__(integer)
