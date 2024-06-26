#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ replaces an element in a list at a specific
    position without modifying the original list (like in C).

    Args:
        my_list (list): original list
        idx (int): index of original element to be replaced
        element (int): element to replace
    return: new list - edited copy of original list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element

    return new_list
