from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = datetime.today().day
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) != o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    return None

def solve_b(inp=input_data):
    return None

tests_a = {
}

a = solve_a()
print(f"Part 1: {a}\n")
# test(tests_a, solve_a)
# submit(a, part="a", day=day, year=2020)

tests_b = {
}

b = solve_b()
if b:
    print(f"Part 2: {b}")
    # test(tests_b, solve_b)
    # submit(b, part="b", day=day, year=2020)
