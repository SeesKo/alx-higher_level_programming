#!/usr/bin/python3
"""
Defines a function that divides all elements of a matrix.

All matrix elements divided by div, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    """

    # Validate matrix input
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    # Validate each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div input
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if all elements are either int or float
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    # Divide all elements by div, rounded to 2 decimal places
    result_matrix = \
        [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
