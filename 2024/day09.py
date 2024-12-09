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

day = 9
puzzle = Puzzle(year=2024, day=day)
inp = """
2333133121414131402
""".strip()
inp = puzzle.input_data
res = 0

idn = 0
s = []
pos = 0
free_blocks = []
files = []
for length, space in seq(list(inp + "0")).map(int).grouped(2):
    s.extend([idn]*length)
    files.append((pos, length))
    pos += length
    s.extend([-1]*space)
    free_blocks.append((pos, space))
    pos += space
    idn += 1

# for i in range(len(s)):
#     # print(seq(s).make_string("").replace("-1", "."))
#     if i > len(s)-1:
#         break
#     while s[i] == -1:
#         s[i] = s.pop()
#
# res = sum(i*x for i,x in enumerate(s))

for p, length in reversed(files):
    for i, (p2, space) in enumerate(free_blocks):
        if space >= length and p >= p2:
            s[p2:p2+length] = s[p:p+length]
            s[p:p+length] = [-1]*length
            free_blocks[i] = (p2+length, space-length)
            break

res = sum(i*x for i,x in enumerate(s) if x != -1)

print(f"Solution: {res}\n")
# submit(res)

print(f"----{time.time()-st:.2f} s----")
