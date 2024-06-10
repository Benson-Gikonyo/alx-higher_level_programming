#!/usr/bin/python3
""" Defines a function add-interger that adds 2 intergers
"""


def add_integer(a, b=98):
    """function to add 2 intergers

    Args:
        a (int): first interger
        b (int): second interger Defaults to 98.
    """

    if isinstance(a, int) or isinstance(a, float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int) or isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
