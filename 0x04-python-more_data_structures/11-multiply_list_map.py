#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    returns a list with all values multiplied
    by a number without using any loops.

    Args:
        my_list (list): list of intergers
        number (int):

    Returns: a new list
        Same length as my_list
        Each value should be multiplied by number
    """
    new_list = list(map(lambda num: num * number, my_list))

    return new_list
