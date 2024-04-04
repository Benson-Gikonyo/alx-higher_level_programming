#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds 2 tuples.

    Args:
        tuple_a (tuple): First tuple.
        tuple_b (tuple): Second tuple.

    Return: new tuple with 2 intergers
    """

    if not tuple_a or len(tuple_a) < 2:
        tuple_a += (0, 0)

    if not tuple_b or len(tuple_b) < 2:
        tuple_b += (0, 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple
