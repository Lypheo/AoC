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

day = 2
puzzle = Puzzle(year=2024, day=day)
inp = puzzle.input_data
inp = lines(inp)
res = 0
def check_safe(nums):
    safe = True
    inc = nums[1] > nums[0]
    for a, b in pairwise(nums):
        if inc:
            safe = safe and b > a
        else:
            safe = safe and b < a
        safe = safe and 1 <= abs(b - a) <= 3
    return safe

for line in inp:
    nums = ints(line)
    safe = check_safe(nums)
    for i in range(len(nums)):
        if safe:
            break
        safe = check_safe(nums[:i] + nums[i+1:])
    res += int(safe)

print(f"Solution: {res}\n")
