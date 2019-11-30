import numpy as np

serial = 7689
grid = np.full((300,300), None)
for x, y in np.ndindex(grid.shape):
    pwl = str(((x + 1 + 10) * (y + 1) + serial) * (x + 10 + 1))
    pwl = int(pwl[-3]) if len(pwl) > 2 else 0
    grid[x,y] = pwl - 5

pwl_grid = np.full((298, 298), None)
for x, y in np.ndindex(pwl_grid.shape):
    sub_grid = grid[y:y+3,x:x+3]
    pwl_grid[x, y] = sub_grid.sum()

largest_pow = np.where(pwl_grid == pwl_grid.max())
print(largest_pow[1][0] + 1, largest_pow[0][0] + 1)
