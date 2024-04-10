#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers.

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.

    return: real number of intergers printed
    """
    try:
        int_printed = 0
        for num in range(x):
            if type(my_list[num]) is int:
                print("{:d}".format(my_list[num]), end="")
                int_printed += 1

    except Exception:
        pass

    print()
    return int_printed
