import re, itertools

_input = open(r"..\..\input.txt").readlines()
regex = re.compile(r"position=< *(-?[0-9]+),  *(-?[0-9]+)> velocity=< *(-?[0-9]+), *(-?[0-9]+)>")

data = [{"pos":parsed[:2], "v":parsed[2:]} for parsed in [list(map(int, regex.match(i).groups())) for i in _input]]

def isText(points):
    for p in points:
        for p2 in points:
            if abs(p[0] - p2[0]) < 2 and abs(p[1] - p2[1]) < 2 and p != p2:
                break
        else:
            return False
    return True

for k in itertools.count():
    points = [(p["pos"][0] + p["v"][0] * k, p["pos"][1] + p["v"][1] * k) for p in data]

    if isText(points):
        minX = min([i[0] for i in points])
        maxX = max([i[0] for i in points]) 
        minY = min([i[1] for i in points])
        maxY = max([i[1] for i in points])
        grid = [[" " for x in range(0, maxX - minX + 1)] for row in range(0, maxY - minY + 1)]

        for p in points:
            grid[p[1] - minY][p[0] - minX] = "□"
        for i in grid:
            print(*i)

        print(k)
        break 