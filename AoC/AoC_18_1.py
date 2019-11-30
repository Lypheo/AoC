import numpy

inp = open(r"input.txt").read().strip("\n").split("\n")
grid = numpy.empty([len(inp), len(inp)], dtype=str)

for y_i,row in enumerate(inp):
    for x_i, x in enumerate(row):
        grid[y_i, x_i] = x

def transform(y,x, old):
    adjacent = []

    for X in range(x and x-1, x+2 if x < len(inp) - 1 else x+1):
        for Y in range(y and y-1, y+2 if y < len(inp) - 1 else y+1):
            adjacent.append(old[Y,X])            

    adjacent.remove(old[y,x])

    if old[y,x] == ".":
        if adjacent.count("|") >= 3:
            return "|"
        else:
            return "."
    elif old[y,x] == "|":
        if adjacent.count("#") >= 3:
            return "#"
        else:
            return "|"
    else:
        if "#" in adjacent and "|" in adjacent:
            return "#"
        else:
            return "."

def timestep():
    old = numpy.copy(grid)
    for iy,ix in numpy.ndindex(old.shape):
        grid[iy,ix] = transform(iy, ix, old)

for i in range(10):
    timestep()

print(("#"==grid).sum()*("|"==grid).sum())