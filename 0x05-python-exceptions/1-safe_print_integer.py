#!/usr/bin/python3
def safe_print_integer(value):
    """
    prints an integer with "{:d}".format().

    Args:
        value (any): value to be printed
    return:
        True if value is printed correctly(is an int)
        False if the value is not printed(not an int)
    """
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise Exception

    except Exception:
        return False
