#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict)
        value (_type_): value to delete key from.
    """
    if (not value) or (value not in a_dictionary.values()):
        return a_dictionary

    del_keys = [key for key, val in a_dictionary.items() if val == value]
    for key in del_keys:
        del (a_dictionary[key])

    return a_dictionary
