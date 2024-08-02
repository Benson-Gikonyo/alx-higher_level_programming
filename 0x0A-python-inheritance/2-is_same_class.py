#!/usr/bin/python3
""" defines is_same_class function"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an
    instance of the specified class ; otherwise False.

    Args:
        obj : object/instance to be checkec
        a_class : class to check against

    Return: bool
    """
    if type(obj) is a_class:
        return True

    return False
