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
day = 6
puzzle = Puzzle(year=2023, day=day)
inp = """

""".strip()
inp = puzzle.input_data
inp = lines(inp)
times = ints(inp[0])
dist = ints(inp[1])

# res = 1
# for t, d in zip(times, dist):
#     valid = 0
#     for charge in range(1, t-1):
#         if (t - charge) * charge > d:
#             valid += 1
#     res *= valid
#
# print(f"Solution: {res}\n")

time = int("".join(str(t) for t in times))
dist = int("".join(str(d) for d in dist))
print(time, dist)
valid = 0
for charge in range(1, time-1):
    if (time - charge) * charge > dist:
        print(valid)
        valid += 1

# (time-x) * x = d
# x^2 - time*x + d = 0
# x1 = time/2 + sqrt(time^2/4 - d)
# x2 = time/2 - sqrt(time^2/4 - d)
# solution = x2 - x1
print(valid)
# submit(valid)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")