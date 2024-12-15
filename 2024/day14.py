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

day =14
puzzle = Puzzle(year=2024, day=day)
inp = """
p=2,4 v=2,-3
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=9,5 v=-3,-3
""".strip()
H,W = 7, 11
inp = puzzle.input_data
H,W = 103, 101

inp = lines(inp)
res = 0

bots = []
for line in inp:
    p = complex(*ints(line)[:2])
    v = complex(*ints(line)[2:])
    bots.append([v, p])

for c in count(1):
    for i, (v, p) in enumerate(bots):
        newp = v + p
        newp = complex(newp.real % W, newp.imag % H)
        bots[i][1] = newp

    if c == 100:
        quads = [0]*4
        for v, p in bots:
            quads[0] += 0 <= p.real < W/2-1 and 0 <= p.imag < H/2-1
            quads[1] += 0 <= p.real < W/2-1 and H/2 < p.imag < H
            quads[2] += W/2 < p.real < W and 0 <= p.imag < H/2-1
            quads[3] += W/2 < p.real < W and H/2 < p.imag < H
        p1 = prod(quads)

    sgrid = {p for v, p in bots}
    if sum(any(k in sgrid for k in nbdc(p)) for p in sgrid) / len(sgrid) > 0.7:
        pgrid(sgrid)
        p2 = c
        break


print(f"Solution: {p1, p2}\n")
copy(res)
# submit(res)

print("----%.2f s----"%(time.time()-st))
