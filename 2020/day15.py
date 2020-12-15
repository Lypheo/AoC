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

day = 15
puzzle = Puzzle(year=2020, day=day)
# input_data = puzzle.input_data
input_data = "0,8,15,2,12,1,4"

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\nInput:\n{i}\nExpected output:\n    {o}\nActual output:\n    ", end="")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data, k = 2020):
    start = [int(x) for x in inp.split(",")]
    nums = collections.defaultdict(list, {x: [i] for i, x in enumerate(start)})
    last = start[-1]

    for i in range(k-len(start)):
        last = 0 if len(nums[last]) <= 1 else nums[last][-1] - nums[last][-2]
        nums[last].append(i+len(start))
        # nums[last] = nums[last][-2:] # redcues ram usage by a couple gigs

    return last

def solve_b(inp=input_data):
    return solve_a(inp, 30000000)

tests = {
"0,3,6": (436, 175594)
}


# a = solve_a()
# print(f"Part 1: {a}\n")
test(tests, solve_a)
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
# t1 = time.time_ns()
# for i in range(times := 1):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")