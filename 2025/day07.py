import os
import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from aocl import *
from functional import seq
from fn import _ as l
from pyperclip import copy

st=time.time()

puzzle = Puzzle(year=2025, day=7)
inp = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()
inp = puzzle.input_data

grid = parse_grid(inp)
pos = {next(pos for pos, val in grid.items() if val == "S"): 1}
Y = int(max(pos.imag for pos in grid.keys()))

for i in range(Y+1):
    next_pos = dd(int)
    for p, num in pos.items():
        p += 1j
        if grid.get(p, ".") == "^":
            next_pos[p + 1] += num
            next_pos[p - 1] += num
        else:
            next_pos[p] += num
    pos = next_pos

res = sum(pos.values())
print(f"Solution: {res}\n")
copy(res)

print(f"----{(time.time()-st):.3f} s----")