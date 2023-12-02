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
day = 1
puzzle = Puzzle(year=2023, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = lines(inp)
    inp = [int(n) for n in lines(inp)]
    return

def solve_b(inp=input_data):
    return False

tests = {
    """""": [None, None]
}

# test(tests, solve_a, 0)
a = solve_a()
print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2023)

# test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2023)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")