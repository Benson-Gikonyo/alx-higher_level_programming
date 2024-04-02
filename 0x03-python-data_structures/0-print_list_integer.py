#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all integers of a list.

    Args:
        my_list (list, optional): list of intergers. Defaults to [].
    """
    for num in range(0, len(my_list)):
        print("{:d}".format(my_list[num]))
