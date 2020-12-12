import time
from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 12
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output:\n")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    ops = [(x[0], int(x[1:])) for x in inp.split("\n")]
    pos = 0j
    cdirs = {"N": 1j, "S": -1j, "E": 1, "W":-1}
    dirs = {"L": 1j, "R": -1j}
    facing = cdirs["E"]
    for op, l in ops:
        facing *= dirs.get(op, 1) ** (l/90)
        pos += facing * l if op == "F" else cdirs.get(op, 0) * l
    return int(abs(pos.real) + abs(pos.imag))

def solve_b(inp=input_data):
    ops = [(x[0], int(x[1:])) for x in inp.split("\n")]
    pos, wpos = 0, 10+1j
    cdirs = {"N": 1j, "S": -1j, "E": 1, "W":-1}
    dirs = {"L": 1j, "R": -1j}
    for op, l in ops:
        wpos += cdirs.get(op, 0) * l
        wpos *= dirs.get(op, 1) ** (l/90)
        if op == "F":
            pos += wpos * l
    return int(abs(pos.real) + abs(pos.imag))

tests = {
    """F10
N3
F7
R90
F11""": (25, 286)
}


a = solve_a()
print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

b = solve_b()
print(f"Part 2: {b}")
# test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")
#
# t1 = time.time_ns()
# for i in range(times := 5):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")