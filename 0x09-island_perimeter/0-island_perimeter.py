#!/usr/bin/python3
""" This function iterates through each cell in the grid. For every land cell (with a value of 1),
 it adds 4 to the perimeter (representing the initial assumption of the land being surrounded by water). 
"""


def island_perimeter(grid):
    """
    Island function
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found land
                perimeter += 4  # Initially, assume full perimeter
                # Check neighbors
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter