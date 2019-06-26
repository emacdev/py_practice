#!/usr/bin/env python

"""
    Compute the median island size
"""


class IslandSolver:
    @staticmethod
    def compute_median(grid):
        """
            For a given i, j in the grid -> check to see if any of it's neighbours are islands. If they are,
            recurse down and increment the cell count, if they aren't return.
        """

        def bfs(isl_grid, i, j):
            if i < 0 or i >= len(isl_grid) or j < 0 or j >= len(isl_grid[0]):
                return 0
            if not isl_grid[i][j]:
                return 0
            else:
                isl_grid[i][j] = 0
                return 1\
                    + bfs(isl_grid, i + 1, j)\
                    + bfs(isl_grid, i, j + 1)\
                    + bfs(isl_grid, i - 1, j) \
                    + bfs(isl_grid, i, j - 1)

        for row in range(len(grid)):
            print(grid[row])

        islands = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                isl_size = bfs(grid, row, col)
                if isl_size:
                    islands.append(isl_size)

        islands.sort()
        print(islands)
        n = len(islands)

        if n % 2 == 0:
            return (islands[n // 2 - 1] + islands[n // 2]) / 2
        else:
            return islands[n // 2]
