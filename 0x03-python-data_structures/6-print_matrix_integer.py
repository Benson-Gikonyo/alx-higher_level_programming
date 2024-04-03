#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    prints a matrix of integers.

    Args:
        matrix (list): matrix to be printed Defaults to [[]].
    """
    if not matrix:
        print("")

    for row in matrix:
        for col in row:
            if col == row[- 1]:
                print("{:d}".format(col), end="")
            else:
                print("{:d} ".format(col), end="")
        print("")
