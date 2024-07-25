#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    function generates and returns the first n rows of Pascal's Triangle as a list of lists, 
    where each inner list represents a row in the triangle.
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k
