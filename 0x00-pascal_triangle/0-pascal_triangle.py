#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal's triangle
    """
    if n <= 0:
        return []
    
    PTriangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, len(PTriangle[-1])):
            row.append(PTriangle[-1][j - 1] + PTriangle[-1][j])
        row.append(1)
        PTriangle.append(row)

    return (PTriangle)