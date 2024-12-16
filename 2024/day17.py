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

# day = 17
# puzzle = Puzzle(year=2024, day=day)
# inp = """
#
# """.strip()
# inp = puzzle.input_data
#
# inp = lines(inp)
# res = 0

N = 10
M = 5

valid = lambda x: 0 <= x.real < N and 0 <= x.imag < M
p = 0
res = 0
@functools.cache
def f(p, seen):
    if len(seen) == N*M:
        return 1
    out = 0
    for n in nbc(p):
        if not valid(n):
            continue
        if n not in seen:
            out += f(n, tuple(sorted([p, *seen], key=lambda x: x.real + 1000*x.imag)))
    return out
res = f(p, tuple())

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print("----%.2f s----"%(time.time()-st))
