#!/usr/bin/python3
"""
Module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
            or if each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rows_sizes = [len(row) for row in matrix]
    if not all(size == rows_sizes[0] for size in rows_sizes):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
