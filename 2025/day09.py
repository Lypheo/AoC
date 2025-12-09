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

puzzle = Puzzle(year=2025, day=9)
inp = """

""".strip()
inp = puzzle.input_data

points = [complex(*ints(line)) for line in lines(inp)]
res = 0
def area(a, b):
    return int(abs(a.real - b.real) + 1) * int(abs(a.imag - b.imag) + 1)

res = max(area(a,b) for a,b in combinations(points, 2))
print(f"Solution: {res}\n")
copy(res)

print(f"----{(time.time()-st):.3f} s----")