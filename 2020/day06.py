from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 6
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True


def solve_a(inp=input_data):
    groups = inp.split("\n\n")
    return sum(len(set(g)-set("\n")) for g in groups)

def solve_b(inp=input_data):
    groups = inp.split("\n\n")
    return sum(all(l in x for x in g.split("\n")) for l in "abcdefghijklmnopqrstuvwxyz" for g in groups)


a = solve_a()
print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

b = solve_b()
if not b:
    exit(0)

print(f"Part 2: {b}")
# test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

import time
t1 = time.time_ns()
for i in range(times := 1000):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(times)} ns")