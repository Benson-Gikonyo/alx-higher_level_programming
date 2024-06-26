#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets.

    Args:
        set_1: second set
        set_2:  second set

    return: set with common elements
    """
    empty = set()
    if not set_1 or len(set_1) == 0:
        return empty
    if not set_2 or len(set_2) == 0:
        return empty

    return set_1 & set_2
