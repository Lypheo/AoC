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

puzzle = Puzzle(year=2024, day=18)
inp = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()
W = 6
inp = lines(inp)[:12]

inp = puzzle.input_data
W = 70
inp = lines(inp)[:]

goal = W + W*1j

def f(grid):
    Q = {0}
    seen = set()
    while Q:
        newQ = set()
        for p in Q:
            seen.add(p)
            if p == goal:
                return True
            for n in nbc(p):
                if n in grid or not (0 <= n.real <= W and 0 <= n.imag <= W) or n in seen:
                    continue
                newQ.add(n)
        Q = newQ
    return False

cgrid = set()
i =0
for line in inp:
    x, y = ints(line)
    cgrid.add(complex(x,y))
    if not f(cgrid):
        res = line
        break
    print(i:=i+1)
    # pgrid(cgrid)

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")