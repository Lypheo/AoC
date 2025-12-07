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
res = 0
pos = {next(pos for pos, val in grid.items() if val == "S")}
Y = int(max(pos.imag for pos in grid.keys()))
for i in range(Y+1):
    # print(pos)
    next_pos = set()
    for p in pos:
        p += 1j
        if grid.get(p, ".") == "^":
            next_pos.update([p - 1, p + 1])
            res += 1
        else:
            next_pos.add(p)
    pos = next_pos

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")