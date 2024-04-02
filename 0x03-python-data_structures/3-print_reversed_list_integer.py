#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ function that prints all integers of a list, in reverse order.

    Args:
        my_list (list):contains intergers.
    Return: nothing.
    """

    if not my_list:
        return None

    for num in range(len(my_list)-1, -1, -1):
        print("{:d}".format(my_list[num]))
