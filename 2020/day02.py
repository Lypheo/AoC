from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 2
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
    c = 0
    for l in inp.split("\n"):
        lo, up, n, pw = re.findall("(\d+)-(\d+) (\w): (\w+)", l)[0]
        lo, up = [int(x) for x in (lo, up)]
        c += int(lo <= pw.count(n) <= up)
    return c

def solve_b(inp=input_data):
    c = 0
    for l in inp.split("\n"):
        lo, up, n, pw = re.findall("(\d+)-(\d+) (\w): (\w+)", l)[0]
        lo, up = [int(x)-1 for x in (lo, up)]
        c += int((pw[lo] == n) != (pw[up] == n))
    return c

tests_a = {
    """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""": 2
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
