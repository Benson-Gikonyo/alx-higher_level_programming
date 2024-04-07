#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    returns the weighted average of all integers tuple
    (score, weight)

    Args:
        my_list (list):
    """
    if len(my_list) == 0:
        return 0

    prod_sum = 0
    weight_sum = 0

    prod_sum = sum(list(map(lambda prod: prod[0] * prod[1], my_list)))
    weight_sum = sum([tupl[1] for tupl in my_list])

    return prod_sum / weight_sum
