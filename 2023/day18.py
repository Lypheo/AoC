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
points = []
for line in inp:
    dir_, c, color = line.split(" ")
    c = int(c)
    color = color.strip("()")[1:]
    c = int(color[:5], 16)
    dir_ = ["R", "D", "L", "U"][int(color[5])]
    points.append(pos)
    d = {"R": 1, "L": -1, "D": 1j, "U": -1j}[dir_]
    pos += c * d
    # for i in range(c):
    #     grid[pos] = "#"
    #     pos += d

print(points)
for p1, p2 in pairwise(points + [points[0]]):
    res += (p1.imag + p2.imag) * (p1.real - p2.real)
    res += abs(p2 - p1)
res /= 2
res += 1
# x1, x2 = min([p.real for p in grid.keys()]), max([p.real for p in grid.keys()])
# y1, y2 = min([p.imag for p in grid.keys()]), max([p.imag for p in grid.keys()])

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")