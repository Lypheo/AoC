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
from functional import seq
from fn import _ as l

day = 4
puzzle = Puzzle(year=2024, day=day)
inp = """

""".strip()
inp = puzzle.input_data

inp = lines(inp)
res = 0
grid = {}
for y, line in enumerate(inp):
    for x, row in enumerate(line):
        grid[x + y*1j] = row

# for pos, c in grid.items():
#     if c != "X":
#         continue
#     for k in nbd(pos):
#         if grid.get(k) == "M":
#             v = k - pos
#             if grid.get(k + v) == "A" and grid.get(k + v*2) == "S":
#                 res += 1

for pos, c in grid.items():
    if c != "A":
        continue
    mas = 0
    for k in nbd(pos):
        if grid.get(k) == "M":
            v = pos - k
            if (v.real != 0 and v.imag != 0) and grid.get(pos + v) == "S":
                mas += 1
    res += mas == 2


print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")