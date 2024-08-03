#!/usr/bin/python3
"""defines the inherits_from() function"""


def inherits_from(obj, a_class):
    """returns True if the object is an
    instance of a class that inherited (directly
    or indirectly) from the specified class ; otherwise False.

    Args:
        obj: object to be checked
        a_class : class to be checked against

    Return: bool
    """

    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    return False
