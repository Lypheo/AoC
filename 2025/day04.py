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

puzzle = Puzzle(year=2025, day=4)
inp = """

""".strip()
inp = puzzle.input_data

grid = parse_grid(inp, to_set=True)
orig_len = len(grid)
while True:
    next_grid = grid.copy()
    for roll in grid:
        if sum(1 for x in nbd(roll) if x in grid) < 4:
            next_grid.remove(roll)
    if grid == next_grid:
        break
    grid = next_grid
res = orig_len - len(grid)

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")