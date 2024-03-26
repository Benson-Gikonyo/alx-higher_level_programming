#!/usr/bin/python3
def print_last_digit(number):
    """_summary_

    Args:
        number (_type_): _description_
    """ 
    
    l_digit = abs(number) % 10
    print(f"{l_digit:d}", end = "")
    
    return l_digit
