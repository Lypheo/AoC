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

puzzle = Puzzle(year=2025, day=5)
inp = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()
inp = puzzle.input_data

fresh, av = blocks(inp)
fresh = [ints(line.replace("-", " ")) for line in lines(fresh)]
av = [int(line) for line in lines(av)]
res = 0
for ing in av:
    for s, e in fresh:
        if s <= ing <= e:
            res += 1
            break
print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")