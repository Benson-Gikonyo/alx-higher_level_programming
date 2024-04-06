#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list.

    Args:
        my_list : list to search and replace in
        search : element to look for
        replace (_type_): element to replace with
    return: new_list
    """

    new_list = my_list.copy()

    indexes = [index for index, num in enumerate(my_list) if num == search]

    for num in range(len(new_list)):
        if num in indexes:
            new_list[num] = replace

    return new_list
