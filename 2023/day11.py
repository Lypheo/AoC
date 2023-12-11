import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
from aocl import *
day = 11
puzzle = Puzzle(year=2023, day=day)
inp = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()
inp = puzzle.input_data

grid = set()
for y, line in enumerate(lines(inp)):
    for x, col in enumerate(line):
        if col == "#":
            grid.add(complex(x, y))

pgrid(grid)

minx,maxx = min([x.real for x in grid]), max([x.real for x in grid])
miny,maxy = min([x.imag for x in grid]), max([x.imag for x in grid])
xoff = []
expand = 1000000-1
for x in sri(minx, maxx):
    xp = [p for p in grid if p.real == x]
    xoff.append(0 if xp else expand)

yoff = []
for y in sri(miny, maxy):
    yp = [p for p in grid if p.imag == y]
    yoff.append(0 if yp else expand)

newgrid = set()
for p in grid:
    x,y = p.real, p.imag
    p = complex(
        x + sum(k for i, k in enumerate(xoff) if i < x),
        y + sum(k for i, k in enumerate(yoff) if i < y),
    )
    newgrid.add(p)

res = 0
for p1, p2 in itertools.combinations(newgrid, r=2):
    res += mh_dist(p1, p2)

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")