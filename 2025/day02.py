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

puzzle = Puzzle(year=2025, day=2)
inp = """

""".strip()
inp = puzzle.input_data

ranges = inp.split(",").seq().map(lambda x: x.split("-")).map(lambda x: (int(x[0]), int(x[1]))).to_list()
res = 0
for start, end in ranges:
    for id_ in range(start, end +1):
        sid = str(id_)
        if len(sid) % 2 == 1:
            continue
        if sid[:len(sid)//2] == sid[len(sid)//2:]:
            res += id_

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")