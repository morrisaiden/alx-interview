#!/usr/bin/python3
"""
perimeter of an island
"""

def island_perimeter(grid):
    """Returns the perimeter of the island described in the grid."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2


    return perimeter
