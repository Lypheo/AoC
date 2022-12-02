import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 2
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    inp = inp.splitlines()
    score = 0
    for l in inp:
        a, b = l.split(" ")
        b = ["X" , "Y", "Z"].index(b)
        a = ["A" , "B", "C"].index(a)
        if b == (a+1) % 3:
            score += (b+1)+6
        elif b == (a+2) % 3:
            score += b+1
        elif b == a:
            score += b+3+1

    return score

def solve_b(inp=input_data):
    inp = inp.splitlines()
    score = 0
    for l in inp:
        a, b = l.split(" ")
        b = ["X" , "Y", "Z"].index(b)
        a = ["A" , "B", "C"].index(a)
        if b == 0:
            score += (a+2) % 3 + 1
        elif b == 1:
            score += a + 3 + 1
        elif b == 2:
            score += (a+1) % 3 + 6 + 1

    return score

tests = {
    """A Y
B X
C Z""": [15, 12]
}

test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")