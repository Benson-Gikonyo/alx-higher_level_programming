#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer).

    Args:
        my_list (list): list containing intergers

    return: sum of unique intergers
    """
    set_list = set(my_list.copy())
    sum = 0
    for num in set_list:
        sum += num

    return sum
