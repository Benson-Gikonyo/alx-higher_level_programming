#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary (dict): dictionary

    return: dictionary with values X 2
    """
    new_dict = a_dictionary.copy()

    for key, value in new_dict.items():
        new_dict[key] = value * 2

    return new_dict
