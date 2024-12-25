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
from pyperclip import copy

st=time.time()

puzzle = Puzzle(year=2024, day=25)
inp = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""".strip()
inp = puzzle.input_data

grids = blocks(inp)
grids = [{k for k,v in parse_grid(g).items() if v == "#"} for g in grids]
keys = [g for g in grids if 0 in g]
locks = [g for g in grids if 0 not in g]
res = 0
for i, key in enumerate(keys):
    for j, lock in enumerate(locks):
        if not (key & lock):
            res += 1
print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")