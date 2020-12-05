from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 5
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
    ps = (re.sub(r"[LF]", "0", re.sub(r"[RB]", "1", x)) for x in inp.split("\n"))
    return max(int(p[:7], 2)*8 + int(p[7:], 2) for p in ps)

def solve_b(inp=input_data):
    ps = (re.sub(r"[LF]", "0", re.sub(r"[RB]", "1", x)) for x in inp.split("\n"))
    ids = [int(p[:7], 2)*8 + int(p[7:], 2) for p in ps]
    for r in range(2**7):
        for c in range(2**3):
            i = r*8 + c
            if i not in ids and i + 1 in ids and i - 1 in ids:
                return i

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

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")