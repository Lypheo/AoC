import math
import time
from datetime import datetime
import time
import functools, itertools, collections, re
from math import ceil, prod, gcd

import numpy as np
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 17
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\nInput:\n{i}\nExpected output:\n    {o}\nActual output:\n    ", end="")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def p(g, layer = 0):
    zero = [c for c in g if c[2] == layer]
    if not zero:
        print(".", end="\n\n")
        return
    mn = (min(x[0] for x in zero), min(x[1] for x in zero))
    mx = (max(x[0] for x in zero), max(x[1] for x in zero))
    print(mn, mx)
    for y in range(mn[1], mx[1]+1):
        for x in range(mn[0], mx[0]+1):
            print("#" if g.get((x,y,layer), False) else ".", end="")
        print("\n", end="")
    print("\n", end="")

def solve_a(inp=input_data):
    grid = [list(x) for x in inp.split("\n")]
    grd = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grd[(x,y,0)] = grid[y][x] == "#"

    def neighbours(c):
        o = []
        for x,y,z in itertools.product((-1, 1, 0), repeat=3):
            a = (x+c[0], y+c[1], z+c[2])
            if a != c:
                o.append(a)
        return o

    for i in range(6):
        start = grd.copy()
        p(grd, -1)
        for c in list(start.keys()) + sum((neighbours(c) for c in start), []):
            nbs = neighbours(c)
            s = sum(start.get(x, False) for x in nbs)
            if start.get(c, False):
                if s not in (2, 3):
                    grd[c] = False
            else:
                if s == 3:
                    grd[c] = True


    return  sum(grd.values())

def solve_b(inp=input_data):
    grid = [list(x) for x in inp.split("\n")]
    grd = {(x,y,0,0): grid[y][x] == "#" for x in range(len(grid[0])) for y in range(len(grid))}

    def vadd(v1, v2):
        return tuple(m+n for m, n in zip(v1, v2))

    def neighbours(c):
        # return [vadd(c, v) for v in itertools.product((-1, 1, 0), repeat=4) if v != (0,)*4]
        return nbs(c, 4)

    def nbs(c, d):
        return [vadd(c, v) for v in itertools.product((-1, 1, 0), repeat=d) if v != (0,)*d]

    for i in range(6):
        start = grd.copy()
        for c in set(list(start.keys()) + sum((neighbours(c) for c in start), [])):
            s = sum(start.get(x, False) for x in neighbours(c))
            if start.get(c, False) and s not in (2, 3):
                grd[c] = False
            elif s == 3:
                grd[c] = True

    return sum(grd.values())

tests = {
""".#.
..#
###""": (112,848)
}


# a = solve_a()
# print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

# b = solve_b()
# print(f"Part 2: {b}")
test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")
#
t1 = time.time_ns()
for i in range(times := 5):
    solve_b()
t2 = time.time_ns()
print(f"Part 2: {(t2-t1)/(1000000*times)} ms")