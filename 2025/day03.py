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

puzzle = Puzzle(year=2025, day=3)
inp = """

""".strip()
inp = puzzle.input_data

inp = lines(inp)
res = 0
num = 12
for line in inp:
    batts = [int(x) for x in line]
    digits = []
    index = -1
    for j in range(num):
        rem = [batts[i] for i in range(index + 1, len(batts) - (num - j - 1))]
        digits.append(max(rem))
        index = rem.index(digits[-1]) + index + 1
    res += int("".join(str(x) for x in digits))


print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")