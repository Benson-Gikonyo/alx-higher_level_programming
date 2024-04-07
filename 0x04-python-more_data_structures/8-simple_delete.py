#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes a key in a dictionary.

    Args:
        a_dictionary (dict): dictionary
        key (str): key to delete

    return a_dictionary
    """
    if key in a_dictionary.keys():
        del (a_dictionary[key])

    return a_dictionary
