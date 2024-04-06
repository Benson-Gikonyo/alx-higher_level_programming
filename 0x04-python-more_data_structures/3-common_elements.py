#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets.

    Args:
        set_1: second set
        set_2:  second set

    return: set with common elements
    """
    if not set_1:
        return set_2
    if not set_2:
        return set_1

    return set_1 & set_2
