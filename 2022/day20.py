import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
import sys
sys.path.append("..")
from aocl import *
day = 20
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    file = [(i, int(n)) for i, n in enumerate(inp.splitlines())]
    for mi in range(len(file)):
        ci = [oi for oi,n in file].index(mi)
        oi, n = file.pop(ci)
        newi = (n + ci) % (len(file))
        file.insert(newi, (oi, n))

    file = [n for i, n in file]
    zindex = file.index(0)
    return sum(file[(i + zindex) % len(file)] for i in [1000, 2000, 3000])

def solve_b(inp=input_data):
    dkey = 811589153
    file = [(i, int(n) * dkey) for i, n in enumerate(inp.splitlines())]
    for _ in range(10):
        for mi in range(len(file)):
            ci = [oi for oi,n in file].index(mi)
            oi, n = file.pop(ci)
            newi = (n + ci) % (len(file))
            file.insert(newi, (oi, n))
    file = [n for i, n in file]
    zindex = file.index(0)
    return sum(file[(i + zindex) % len(file)] for i in [1000, 2000, 3000])
tests = {
    """1
2
-3
3
-2
0
4""" : [3, 1623178306]
}

test(tests, solve_a, 0)
a = solve_a()
print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)
#
test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")