#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list.

    Args:
        my_list (list): list 
        idx (int): position of index to remove
    return: my_list
    """
    if abs(idx) > len(my_list):
        return my_list
    
    del(my_list[idx])
    return my_list