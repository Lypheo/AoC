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

ranges, av = blocks(inp)
ranges = [tuple(ints(line.replace("-", " "))) for line in lines(ranges)]
av = [int(line) for line in lines(av)]

ranges = sorted(ranges)

res = 0
last_end = 0
for start, end in ranges:
    start = max(start, last_end+1)
    if end > last_end:
        res += end - start + 1
        last_end = end

ranges = sorted(ranges)
def f(current, next):
    out, last_end = current
    start, end = next
    return out + max(end - max(start, last_end+1) + 1, 0), max(end, last_end)
res = functools.reduce(f, ranges, (0,0))[0]


print(f"Solution: {res}\n")
copy(res)

print(f"----{(time.time()-st):.3f} s----")