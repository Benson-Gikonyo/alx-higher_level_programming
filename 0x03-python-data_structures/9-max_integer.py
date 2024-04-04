#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function that finds the biggest integer of a list.
    Args:
        my_list (list): list of intergers
    return: biggest number
    """

    if not my_list:
        return None

    my_list.sort()

    return my_list[-1]
