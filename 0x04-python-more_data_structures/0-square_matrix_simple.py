#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    computes the square value of all integers of a matrix.

    Args:
        matrix (list): 2 dimensional array

    Return: a new matrix, each value a square of the input
    """
    if not matrix:
        return None

    new_matrix = []
    new_row = []
    for row in matrix:
        new_row = list(map(lambda x: x**2, row))
        new_matrix.append(new_row)

    return new_matrix
