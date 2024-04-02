#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ function that prints all integers of a list, in reverse order.

    Args:
        my_list (list):contains intergers.
    Return: nothing.
    """
    rev_list = my_list.copy()

    for num in range(len(rev_list)-1, -1, -1):
        print("{}".format(rev_list[num]))
