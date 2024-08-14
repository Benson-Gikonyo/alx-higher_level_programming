#!/usr/bin/python3
"""Defines MyList Class"""


class MyList(list):
    """ Mylist class
    """
    def print_sorted(self):
        """prints a sorted list.
        list elements are always int.
        """
        print(sorted(self))
