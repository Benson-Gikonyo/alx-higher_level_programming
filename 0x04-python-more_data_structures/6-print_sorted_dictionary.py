#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): dictionary with ordered keys
    """
    sorted_dict = dict(sorted(a_dictionary.items()))

    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
