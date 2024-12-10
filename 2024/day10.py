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
st=time.time()

day = 10
puzzle = Puzzle(year=2024, day=day)
inp = """
0123
1234
8765
9876
""".strip()
inp = puzzle.input_data

grid = parse_grid(inp, to_int=True)
p1, p2 = 0,0

def f(p, v):
    if v == 9:
        nines.add(p)
        return 1
    return sum(f(x, v+1) for x in nb(p) if grid.get(x) == v+1)

for p, v in grid.items():
    if v == 0:
        nines = set()
        p2 += f(p, v)
        p1 += len(nines)

print(f"Solution: {p1, p2}\n")
# submit(res)

print("----%.2f s----"%(time.time()-st))
