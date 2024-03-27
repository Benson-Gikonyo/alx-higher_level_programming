#!/usr/bin/python3
def remove_char_at(str, n):
    """ creates a copy of the string, removing the character at the position n

    Args:
        str (string): _description_
        n (int): index/position of the number
    """

    new_str = ""

    if n > len(str):
        return str

    for index in range(0, len(str)):
        if index == n:
            continue
        new_str += str[index]

    return new_str
