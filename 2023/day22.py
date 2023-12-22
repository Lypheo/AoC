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
import time
t1 = time.time_ns()
inp = lines(inp)
res = 0
bricks = []
for line in inp:
    s, e = line.split("~")
    s = tuple(int(x) for x in s.split(","))
    e = tuple(int(x) for x in e.split(","))
    bricks.append(((complex(*s[:2]), s[2]), (complex(*e[:2]), e[2])))

bricks.sort(key=lambda p: min(p[0][1], p[1][1]))
fallen_bricks = []
def zs_below(s, e, fallen):
    r = set(ipl(s[0], e[0]))
    curz = max(s[1], e[1])
    out = 0
    for ss, ee in fallen:
        z = max(ss[1], ee[1])
        if z >= curz:
            continue
        if set(ipl(ss[0], ee[0])) & r:
            out = max(out, z)
    return out

def drop(brick, fallen):
    s, e = brick
    below = zs_below(s, e, fallen)
    z = 1 + below
    zd = min(s[1] - z, e[1] - z)
    return (s[0], s[1] - zd), (e[0], e[1] - zd)

while bricks:
    fallen_bricks.append(drop(bricks.pop(0), fallen_bricks))

rests_on = dd(list) # top -> bottom
supports = dd(list) # bottom -> top
for s, e in fallen_bricks:
    possible_contacts = set((p, zz-1) for p in ip(s[0], e[0]) for zz in sri(s[1], e[1]))
    if s[1] != e[1]:
        possible_contacts = {min(possible_contacts, key=lambda x: x[1])}

    for ss, ee in fallen_bricks:
        cubes = set((p, zz) for p in ip(ss[0], ee[0]) for zz in sri(ss[1], ee[1]))
        overlap = cubes & possible_contacts
        if overlap:
            rests_on[(s, e)].append((ss, ee))
            supports[(ss, ee)].append((s, e))

part1 = len(fallen_bricks)
for s, e in fallen_bricks:
    for ss, ee in fallen_bricks:
        foundation = rests_on[(ss, ee)]
        if len(foundation) == 1 and foundation[0] == (s, e):
            part1 -= 1
            break

print(f"Part 1: {part1}")

for bottom in supports.copy():
    dropped = {bottom}
    tops = set(supports[bottom])
    while tops:
        new_drops = set()
        for top in tops:
            foundation = rests_on[top]
            if all(supporter in dropped for supporter in foundation):
                new_drops.add(top)

        tops = set().union(*(set(supports[top]) for top in new_drops))
        dropped.update(new_drops)

    res += len(dropped) - 1

print(f"Part 2: {res}\n")
# submit(res)

# for i in range(times := 1000):
#     solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/1000000} ms")