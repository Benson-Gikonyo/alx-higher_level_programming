#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    function that prints x elements of a list.

    Args:
        my_list (list): list of elements of any type Defaults to [].
        x (int, optional): number of elements to print

    Return: the real number of elements printed
    """
    try:
        num_printed = 0
        for num in range(x):
            print(my_list[num], end="")
            num_printed += 1

    except Exception:
        pass

    print()
    return num_printed
