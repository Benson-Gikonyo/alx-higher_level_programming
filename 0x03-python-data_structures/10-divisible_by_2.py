#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Write a function that finds all multiples of 2 in a list.

    Args:
        my_list (list): list with multiples of 2

    return: new list with True or False
    """
    bool_list = []
    if not my_list:
        return None
    
    for num in range(0, len(my_list)):
        if my_list[num] % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    
    return bool_list
