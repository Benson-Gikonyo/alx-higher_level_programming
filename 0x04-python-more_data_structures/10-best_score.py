#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value.

    Args:
        a_dictionary (dict): dictionary - all values are intergers

    return: key
    """
    if not a_dictionary:
        return None

    values_list = list(a_dictionary.values())
    key_list = list(a_dictionary.keys())
    max_val = max(values_list)
    max_val_index = values_list.index(max_val)
    return key_list[max_val_index]
