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

day = 18
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\nInput:\n{i}\nExpected output:\n    {o}\nActual output:\n    ", end="")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    def evaluate(e):
        def find_pe(e):
            s = 0
            for i in range(len(e)):
                s += int(e[i] == "(")
                s -= int(e[i] == ")")
                if s == -1: return i

        while paran := re.search("\(", e):
            ps = paran.span(0)[0]
            pe = find_pe(e[ps+1:]) + ps + 2
            e = e[:ps] + evaluate(e[ps+1:pe-1]) + e[pe:]

        while sub := re.search("\d+ [+*] \d+", e):
            e = str(eval(sub[0])) + e[sub.span(0)[1]:]

        return e
    return sum(int(evaluate(e)) for e in inp.split("\n"))

def solve_b(inp=input_data):
    def evaluate(e):
        def find_pe(e):
            s = 0
            for i in range(len(e)):
                s += int(e[i] == "(")
                s -= int(e[i] == ")")
                if s == -1: return i

        while paran := re.search("\(", e):
            ps = paran.span(0)[0]
            pe = find_pe(e[ps+1:]) + ps + 2
            e = e[:ps] + evaluate(e[ps+1:pe-1]) + e[pe:]

        for os in ("+", "*"):
            while sub := re.search(rf"\d+ \{os} \d+", e):
                ss, se = sub.span(0)
                e = e[:ss] + str(eval(sub[0])) + e[se:]

        return e
    return sum(int(evaluate(e)) for e in inp.split("\n"))

tests = {
"""1 + (2 * 3) + (4 * (5 + 6))""": (51, )
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
t1 = time.time_ns()
for i in range(times := 100):
    solve_b()
t2 = time.time_ns()
print(f"Part 2: {(t2-t1)/(1000000*times)} ms")