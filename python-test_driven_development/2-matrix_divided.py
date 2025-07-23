#!/usr/bin/python3
"""
This module defines a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers/floats.
        div (int or float): The number to divide each element by.

    Returns:
        list of lists: A new matrix with results rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or rows are not the same size,
                   or div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = list(map(len, matrix))
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]

