import time
from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 9
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data, a = 25):
    nums = [int(x) for x in inp.split("\n")]
    def f(i):
        return i < a or any(k + l == nums[i] for k in nums[i-a:i] for l in nums[i-a:i])

    for i in range(len(nums)):
        if not f(i):
            return nums[i]


def solve_b(inp=input_data, a = 25):
    p1 = solve_a(input_data, a)
    nums = [int(x) for x in input_data.split("\n")]
    nums.reverse()
    sums = []
    for n in nums:
        sums.append(n)
        s = sum(sums)
        if s < p1:
            continue
        elif s == p1 and len(sums) > 1:
            return min(sums) + max(sums)
        else:
            del sums[0]

    return None


tests = {
    """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""" : (127, 62)
}


a = solve_a()
print(f"Part 1: {a}\n")
# test(tests, lambda x : solve_a(x, 5))
# submit(a, part="a", day=day, year=2020)

b = solve_b()
print(f"Part 2: {b}")
# test(tests, lambda x : solve_b(x, 5))
# submit(b, part="b", day=day, year=2020)

t1 = time.time_ns()
for i in range(times := 100):
    solve_a()
t2 = time.time_ns()
print(f"Part 1: {(t2-t1)/(1000000*times)} ms")

t1 = time.time_ns()
for i in range(times := 10000):
    solve_b()
t2 = time.time_ns()
print(f"Part 2: {(t2-t1)/(1000000*times)} ms")