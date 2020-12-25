import math
import time
from datetime import datetime
import time
import functools, itertools, collections, re
from math import ceil, prod, gcd
from collections import defaultdict
cprod = itertools.product

from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 25
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
    card, door = [int(x) for x in inp.split("\n")]
    def transform(loops, sn):
        o = 1
        for _ in range(loops):
            o = (o*sn) % 20201227
        return o

    loopn = []
    for i in (card, door):
        ln = 0
        o = 1
        while o != i:
            ln += 1
            o = (o*7) % 20201227
        loopn.append(ln)

    return transform(loopn[0], door), transform(loopn[1], card)


def solve_b(inp=input_data):
    return None

tests = {
}


a = solve_a()
print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)
#
# b = solve_b()
# print(f"Part 2: {b}")
# test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")


#
# t1 = time.time_ns()
# for i in range(times := 1):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")