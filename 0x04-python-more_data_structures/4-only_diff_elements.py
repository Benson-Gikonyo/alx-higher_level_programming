#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    returns a set of all elements present in only one set.

    Args:
        set_1: first set
        set_2: second set

    return : set difference
    """
    empty = set()
    if not set_1 or len(set_1) == 0:
        return empty
    if not set_2 or len(set_2) == 0:
        return empty

    return set_1 ^ set_2
