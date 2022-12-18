import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from aocl import *

day = 18
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = inp.splitlines()
    drops = set()
    for l in inp:
        x,y,z = ints(l)
        drops.add((x,y,z))
    ans = 0
    for x,y,z in drops:
        adj = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1),(x, y, z-1)]
        ans += sum(1 for cube in adj if cube not in drops)
    return ans

def solve_b(inp=input_data):
    inp = inp.splitlines()
    drops = set()
    for l in inp:
        x,y,z = ints(l)
        drops.add((x,y,z))
    ans = 0
    mins = [min([cube[i] for cube in drops]) for i in range(3)]
    maxs = [max([cube[i] for cube in drops]) for i in range(3)]
    def rd(cube, d, n):
        cube = list(cube)
        cube[d] = n
        return tuple(cube)

    # not a general solution
    # relies on the lava not having any branched holes/caves
    for x,y,z in drops:
        adj = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1),(x, y, z-1)]
        for side in adj:
            if side not in drops and \
                any(
                    all(rd(side, d, n) not in drops for n in sr(side[d], maxs[d], inc=True)) or
                    all(rd(side, d, n) not in drops for n in sr(side[d], mins[d], inc=True))
                    for d in [0,1,2]
                ):
                ans += 1
    return ans
tests = {
    """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""" :[64, 58]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)
#
test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")