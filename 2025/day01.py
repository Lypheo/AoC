import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
# add parent dir to path
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from aocl import *
from functional import seq
from fn import _ as l
from pyperclip import copy

st=time.time()

puzzle = Puzzle(year=2025, day=1)
inp = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()
inp = puzzle.input_data

inp = lines(inp)
p1 = 0
p2 = 0
curr = 50
for line in inp:
    dir = line[0]
    val = int(line[1:])
    val = val if dir == "R" else -val
    p2 += abs((curr + val) // 100)
    if curr == 0 and dir == "L":
        p2 -= 1
    curr = (curr + val) % 100
    if curr == 0:
        p1 += 1
        p2 += dir == "L"

print(f"Part 1: {p1}\n")
print(f"Part 2: {p2}\n")
copy(p2)

print(f"----{(time.time()-st):.3f} s----")