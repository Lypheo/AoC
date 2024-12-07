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

day = 6
puzzle = Puzzle(year=2024, day=day)
inp = """
""".strip()
# inp = puzzle.input_data

res = 0
grid = parse_grid(inp)
orig_pos = seq(grid.keys()).find(lambda k: grid[k] == "^")
def check_loop(obs_pos, p1=False):
    pos = orig_pos
    dr = -1j
    path = set()
    while pos in grid:
        if (pos, dr) in path:
            return True
        path.add((pos, dr))
        while grid.get(pos + dr) == "#" or pos + dr == obs_pos:
            dr *= 1j
        pos += dr
    return False if not p1 else {x[0] for x in path}

orig_path = check_loop(-1-1j, True)
res = seq(grid.keys()).filter(l != orig_pos).filter(orig_path.__contains__).filter(check_loop).len()
print(f"Solution: {len(orig_path)}, {res}\n")
# submit(res)