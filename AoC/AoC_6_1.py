import re, itertools

points = []
with open(r"..\..\input.txt") as _input:
	for j,i in enumerate(_input):
		points.append([int(i) for i in re.compile(r"(\d+), (\d+)").match(i.strip("\n")).groups()] + [j])

x_min, x_max, y_min, y_max = min(points, key=lambda p:p[0])[0], max(points, key=lambda p:p[0])[0], min(points, key=lambda p:p[1])[1], max(points, key=lambda p:p[1])[1]

grid = [[[x,y, None] for x in range(x_min, x_max+1)] for y in range(y_min, y_max+1)]

for x_i, x in enumerate(grid):
	for p_i, p in enumerate(x):
		distances = {}
		for x_2, y_2, k in points:
			distances[k] = abs(p[0] - x_2) + abs(p[1] - y_2)
		grid[x_i][p_i][2] = min(distances, key = lambda key:distances[key])

nearests = {k: 0 for k in range(0, len(points))}
for x in grid:
	for p in x:
		nearests[p[2]] += 1

#fuck efficiency, copy paste ftw

x_min, x_max, y_min, y_max = x_min - 1, x_max + 1, y_min - 1, y_max + 1
grid_2 = [[[x,y, None] for x in range(x_min-1, x_max+2)] for y in range(y_min-1, y_max+2)]

for x_i, x in enumerate(grid_2):
	for p_i, p in enumerate(x):
		distances = {}
		for x_2, y_2, k in points:
			distances[k] = abs(p[0] - x_2) + abs(p[1] - y_2)
		grid_2[x_i][p_i][2] = min(distances, key = lambda key:distances[key])

nearests_2 = {k: 0 for k in range(0, len(points))}
for x in grid_2:
	for p in x:
		nearests_2[p[2]] += 1

non_infinite = [[p,v] for p,v in nearests_2.items() if nearests[p] == v]

print(max(non_infinite, key=lambda x:x[1])) # part one

