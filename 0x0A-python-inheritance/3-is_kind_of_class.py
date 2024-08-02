#!/usr/bin/python3
"""defines is_kind_of_class() function """


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False.

    Args:
        obj: object/instance to be checked
        a_class: class to be checked against.
    """
    if isinstance(obj, a_class):
        return True
    return False
