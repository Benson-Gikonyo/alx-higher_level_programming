#!/usr/bin/python3
def print_last_digit(number):
    """print the last digit of a number

    Args:
        number (number): number to be checked
    Return: the last digit of the number
    """

    l_digit = abs(number) % 10
    print(f"{l_digit:d}", end="")

    return l_digit
