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

puzzle = Puzzle(year=2025, day=6)
inp = """

""".strip()
inp = puzzle.input_data

inp = [line.split() for line in lines(inp)]
n = len(inp[0])
res = 0
tasks = [[line[j] for line in inp] for j in range(n)]
for task in tasks:
    if task[-1] == "+":
        res += sum(int(x) for x in task[:-1])
    else:
        res += prod(int(x) for x in task[:-1])

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")