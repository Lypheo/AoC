test1 = """.#..#
.....
#####
....#
...##"""

test2 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

test3 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""

test4 = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##"""


from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
from timeit import timeit
from fractions import Fraction
from math import copysign
import pprint, math

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    grid = inp.splitlines()
    grid = [list(row) for row in grid]

    def los(a, b, x, y):
        difx, dify = x-a, y-b
        twod = difx != 0 and dify != 0
        if twod:
            delta = Fraction(difx, dify)
            dx, dy = delta.numerator, delta.denominator
        else:
            dx, dy = 1 if difx != 0 else 0, 1 if dify != 0 else 0
        dx, dy = int(copysign(dx, difx)), int(copysign(dy, dify))
        for i in range(1, int((difx)/dx) if twod else max(abs(difx), abs(dify))):
            if grid[i*dy + b][i*dx + a] == "#":
                return False
        return True

    h, w = len(grid), len(grid[0])
    counts = [0] * w*h

    def detections(a, b):
        count = 0
        detected = []
        for y,row in enumerate(grid):
            for x, ast in enumerate(row):
                if ast == "." or (y == b and x == a):
                    continue
                if los(a, b, x, y):
                    count += 1
                    detected.append((x,y))
        return count, detected

    def angle(p, base):
        x, y = p
        x = x - base[0]
        y = base[1] - y
        # print(x, y)
        a = math.atan2(x, y)
        if a < 0:
            # print(2*math.pi + a, p)
            return 2*math.pi + a
        else:
            # print(a, p)
            return a

    for y,row in enumerate(grid):
        for x, ast in enumerate(row):
            if ast == "#":
                counts[y*h + x] = detections(x, y)[0]

    p1 = max(counts)
    station = counts.index(p1)
    station = (station % h, station // h)
    destroyed = []
    visible = detections(*station)[1]
    # print(angle((11,12), station))
    while True:
        if len(visible) == 0:
            break
        destroy = sorted(visible, key=lambda p: angle(p, station))
        # print(destroy)
        destroyed.extend(destroy)
        for x,y in destroy:
            grid[y][x] = "."
        visible = detections(*station)[1]

    return p1, destroyed[199]

a, b = solve()
print(f"Part 1: {a}")
if b: print(f"Part 2: {b}")