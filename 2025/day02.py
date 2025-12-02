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
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
""".strip()
inp = puzzle.input_data

ranges = inp.split(",").seq().map(lambda x: x.split("-")).map(lambda x: (int(x[0]), int(x[1]))).to_list()
res = 0
for start, end in ranges:
    for id_ in range(start, end +1):
        sid = str(id_)
        for i in range(2, len(sid) + 1):
            if len(sid) % i != 0:
                continue
            ss = len(sid)//i
            parts = [sid[j : j + ss] for j in range(0, len(sid), ss)]
            if len(set(parts)) == 1:
                res += id_
                break

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")