import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 3
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) != o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    inp = inp.splitlines()
    o = ""
    o2 = ""
    for i in range(len(inp[0])):
        n = 0
        for l in inp:
            n += 1 if l[i] == "1" else -1
        o += "1" if n > 0 else "0"
        o2 += "0" if n > 0 else "1"

    return int(o, 2) * int(o2, 2)

def solve_b(inp=input_data):
    inp = inp.splitlines()
    numbers = inp.copy()
    for i in range(len(inp[0])):
        Is = [x[i] for x in numbers]
        b = "1" if Is.count("1") >= Is.count("0") else "0"
        numbers = [x for x in numbers if x[i] == b]
        if len(numbers) == 1: break

    o1 = numbers[0]
    numbers = inp.copy()
    for i in range(len(inp[0])):
        Is = [x[i] for x in numbers]
        b = "0" if Is.count("1") >= Is.count("0") else "1"
        numbers = [x for x in numbers if x[i] == b]
        if len(numbers) == 1: break

    o2 = numbers[0]
    return int(o1, 2) * int(o2, 2)

tests_a = {
    """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""" : 198
}

test(tests_a, solve_a)
a = solve_a()
print(f"Part 1: {a}\n")
# submit(a, part="a", day=day, year=2021)

tests_b = {
    """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""" : 230
}

test(tests_b, solve_b)
b = solve_b()
if b:
    print(f"Part 2: {b}")
    submit(b, part="b", day=day, year=2021)
