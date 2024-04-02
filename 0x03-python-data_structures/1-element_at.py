#!/usr/bin/python3
def element_at(my_list, idx):
    """retrieves an element from a list like in C.

    Args:
        my_list (list): C-like list of elements
        idx (int): index where to extract element from my_list
    """
    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]
