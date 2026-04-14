import numpy as np

def create_grid():
    grid = np.zeros((10, 10))

    # obstacles
    grid[3, 3:7] = 1
    grid[6, 2:5] = 1

    start = (0, 0)
    goal = (9, 9)

    return grid, start, goal