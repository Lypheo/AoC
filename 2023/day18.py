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
day = 18
puzzle = Puzzle(year=2023, day=day)
inp = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip()
inp = puzzle.input_data


inp = lines(inp)
res = 0

pos = 0
grid = {}
for line in inp:
    dir_, c, color = line.split(" ")
    c = int(c)
    color = color.strip("()")
    for i in range(c):
        d = {"R": 1, "L": -1, "D": 1j, "U": -1j}[dir_]
        # grid[pos] = color
        grid[pos] = "#"
        pos += d

pgrid(grid)
x1, x2 = min([p.real for p in grid.keys()]), max([p.real for p in grid.keys()])
y1, y2 = min([p.imag for p in grid.keys()]), max([p.imag for p in grid.keys()])

q = [x1 -1 + y1*1j -1j]
outside = set()
seen = set(q)
while q:
    c = q.pop()
    outside.add(c)
    for p in nbd(c):
        if x1-1 <= p.real <= x2+1 and y1-1 <= p.imag <= y2+1 and p not in grid and p not in seen:
            q.append(p)
            seen.add(p)
outside = {p for p in outside if x1 <= p.real <= x2 and y1 <= p.imag <= y2}
res = (x2+1-x1)* (y2+1-y1) - len(outside)


print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")