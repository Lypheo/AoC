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
inp = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
inp = puzzle.input_data

inp = lines(inp)
Y, X = len(inp), len(inp[0])
res = 0

sep = [" "]*Y
tasks = [[inp[y][x] for y in range(Y)] for x in range(X)] + [sep]

op = ""
while True:
    if sep not in tasks:
        break
    i = tasks.index(sep)
    task = tasks[:i]
    op = task[0][-1]
    nums = [int("".join(x for x in el if x.isnumeric())) for el in task]
    res += sum(nums) if op == "+" else prod(nums)
    tasks = tasks[i+1:]

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")