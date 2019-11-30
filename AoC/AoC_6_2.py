import re, itertools

points = []
with open(r"..\..\input.txt") as _input:
	for i in _input:
		points.append([int(i) for i in re.compile(r"(\d+), (\d+)").match(i.strip("\n")).groups()])

x_min, x_max, y_min, y_max = min(points, key=lambda p:p[0])[0], max(points, key=lambda p:p[0])[0], min(points, key=lambda p:p[1])[1], max(points, key=lambda p:p[1])[1]
grid = [[[x,y] for x in range(x_min, x_max+1)] for y in range(y_min, y_max+1)]

within_region = 0

for row_i, row in enumerate(grid):
	for p_i, p in enumerate(row):
		distance = 0
		for x, y in points:
			distance += abs(p[0] - x) + abs(p[1] - y)
		if distance < 10000:
			within_region += 1

print(within_region)

