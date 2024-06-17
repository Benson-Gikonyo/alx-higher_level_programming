#!/usr/bin/python3
""" contains the function  print_square(size)"""


def print_square(size):
    """print a square of size 'size' with #

    Args:
        size (int): size of square

    Return: Nothing
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    else:
        for row in range(0, size):
            for col in range(0, size):
                print("#", end='')
            print("")
