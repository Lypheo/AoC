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
day = 22
puzzle = Puzzle(year=2023, day=day)
inp = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".strip()
inp = puzzle.input_data

inp = lines(inp)
res = 0
bricks = []
maxz = 0
for line in inp:
    s, e = line.split("~")
    s = tuple(int(x) for x in s.split(","))
    e = tuple(int(x) for x in e.split(","))
    maxz = max([maxz, s[2], e[2]])
    bricks.append(((complex(*s[:2]), s[2]), (complex(*e[:2]), e[2])))

bricks.sort(key=lambda p: min(p[0][1], p[1][1]))
fallen_bricks = []
def zs_below(s, e, fallen):
    r = set(ipl(s[0], e[0]))
    curz = max(s[1], e[1])
    out = {}
    for ss, ee in fallen:
        z = max(ss[1], ee[1])
        if z >= curz:
            continue
        for p in set(ipl(ss[0], ee[0])) & r:
            out[p] = max(out.get(p, 0), z)
    assert all(p in r for p in out.keys())
    return out

def drop(brick, fallen):
    s, e = brick
    below = zs_below(s, e, fallen)
    # if brick == (((1+0j), 1), ((1+2j), 1)):
        # print(below)
    if not below:
        z = 1
    else:
        z = max(below.values()) + 1
    zd = min(s[1] - z, e[1] - z)
    return (s[0], s[1] - zd), (e[0], e[1] - zd)

while bricks:
    fallen_bricks.append(drop(bricks.pop(0), fallen_bricks))

# grid = {}
# for s, e in fallen_bricks:
#     for p in ip(s[0], e[0]):
#         for zz in sri(s[1], e[1]):
#             grid[complex(p.imag, zz)] = "#"
# pgrid(grid, zero="bot")

for s, e in fallen_bricks:
    new_fallen = [x for x in fallen_bricks if x != (s, e)]
    for ss, ee in new_fallen:
        d = drop((ss, ee), new_fallen)
        if d != (ss, ee):
            break
    else:
        res += 1

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")