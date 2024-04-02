#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific position (like in C).

    Args:
        my_list (list): list of elements
        idx (int): index of element to be replaced
        element (int): element to replace
        Return: my_list- newly edited
    """

    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
