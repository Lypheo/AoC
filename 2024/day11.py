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

day = 11
puzzle = Puzzle(year=2024, day=day)
inp = """
125 17
""".strip()
inp = puzzle.input_data

@functools.lru_cache(None)
def f(x, cnt):
    if cnt == 0:
        return 1
    nxt = []
    if x == 0:
        nxt.append(1)
    elif len(str(x)) % 2 == 0:
        l, r = str(x)[:len(str(x))//2], str(x)[len(str(x))//2:]
        nxt.extend([int(l), int(r)])
    else:
        nxt.append(x*2024)
    return sum(f(y, cnt - 1) for y in nxt)

inp = ints(inp)
res = sum(f(x, 75) for x in inp)

print(f"Solution: {res}\n")
# submit(res)

print("----%.2f s----"%(time.time()-st))
