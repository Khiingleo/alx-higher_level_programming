#!/usr/bin/python3
"""Defines a pascal_triangle function"""


def pascal_triangle(n):
    """
    creates a pascal's triangle
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                # the first and last numbers in each row always 1
                row.append(1)
            else:
                # calculate the number as the sum of the
                # two numbers above it
                prev_row = triangle[i - 1]
                num = prev_row[j - 1] + prev_row[j]
                row.append(num)
        triangle.append(row)
    return triangle
