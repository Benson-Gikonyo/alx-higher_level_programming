#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides 2 integers and prints the result.

    Args:
        a (int): 1st interger
        b (int): 2nd interger

    Returns: division value or none
    """
    quotient = None
    try:
        quotient = a / b

    except Exception:
        return quotient

    finally:
        print("Inside result: {}".format(quotient))
        return quotient
