#!/usr/bin/python3
"""_summary_"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of size n:

    Args:
        n (int): size of triangle

    Return: list
    """
    if n < 1:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
