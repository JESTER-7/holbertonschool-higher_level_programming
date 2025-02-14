#!/usr/bin/python3
"""file"""


def pascal_triangle(n):
    """PRINT PASCAL TRIANGLE"""

    triangle = []
    if n <= 0:
        return []
    triangle.append([1])
    for i in range(1, n):
        prev = triangle[i - 1]
        new = [1]
        for j in range(len(prev) - 1):
            new.append(prev[j] + prev[j + 1])
        new.append(1)
        triangle.append(new)
    return triangle
