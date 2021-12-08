import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 1
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    inp = inp.splitlines()
    inp = [int(n) for n in inp.splitlines()]
    return

def solve_b(inp=input_data):
    return False

tests = {
}

# test(tests, solve_a, 0)
a = solve_a()
print(f"Part 1: {a}\n")
submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

# test(tests, solve_b, 1)
# b = solve_b()
# if b:
#     print(f"Part 2: {b}")
#     submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")