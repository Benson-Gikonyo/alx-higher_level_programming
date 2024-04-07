#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (_type_): _description_
        key (string): _description_
        value (any type): _description_

    return: updated dictionary
    """
    if not a_dictionary:
        a_dictionary = dict(key, value)

    if (key in a_dictionary.keys()) or (key not in a_dictionary.keys()):
        a_dictionary[key] = value

    return a_dictionary
