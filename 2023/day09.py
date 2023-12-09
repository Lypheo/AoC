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
day = 9
puzzle = Puzzle(year=2023, day=day)
inp = """

""".strip()
inp = puzzle.input_data


inp = lines(inp)
res = 0

for line in inp:
    hist = list(reversed(ints(line)))
    diff = hist.copy()
    diffs = [diff.copy()]
    while not all(x == 0 for x in diff):
        assert diff
        diff = [x-y for y, x in pairwise(diff)]
        diffs.append(diff.copy())
    x = diff[-1]
    for d in reversed(diffs):
        x += d[-1]
    res += x
print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")