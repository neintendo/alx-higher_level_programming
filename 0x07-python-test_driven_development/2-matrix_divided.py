#!/usr/bin/python3
"""
This module provides a function that divides all elements in a matrix.

Usage:
    matrix_divided = __import__('2-matrix_divided').matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: the matrix.
        div: the value to divide elements of the matrix by.

    Return: a new copy of matrix with values divided by div.
    """
    # Checks if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check for zero division error.
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Check if elements are int/float or not.
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    # Check if each row is the same size
    row_len = len(matrix[0])
    for a in range(len(matrix)):
        if len(matrix[a]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Create a copy of the matrix
    matrix_copy = [[element for element in row] for row in matrix]

    rr = 0
    for row in matrix_copy:
        ee = 0
        for element in row:
            matrix_copy[rr][ee] = round(element / div, 2)
            ee += 1
        rr += 1

    return matrix_copy
