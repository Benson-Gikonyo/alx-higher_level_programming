#!/usr/bin/Python3
def no_c(my_string):
    """
    removes all characters c and C from a string.

    Args:
        my_string (str): string to extract c and C from

    return: my_string - edited
    """
    new_string = ""

    for num in range(0, len(my_string)):
        if my_string[num] == 'c' or my_string[num] == 'C':
            continue
        else:
            new_string += my_string[num]

    return new_string
