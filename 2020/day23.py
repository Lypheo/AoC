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

day = 23
puzzle = Puzzle(year=2020, day=day)
# input_data = puzzle.input_data
input_data = "916438275"

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\nInput:\n{i}\nExpected output:\n    {o}\nActual output:\n    ", end="")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    cupsl = [int(x) for x in inp]
    l = len(cupsl)
    cups = {}
    for i in range(len(cupsl)):
        cups[cupsl[i]] = cupsl[(i+1) % l]

    current = cupsl[0]
    mn, mx = min(cups), max(cups)
    for _ in range(100):
        pickup = [cups[current]]
        for i in range(2):
            pickup.append(cups[pickup[i]])

        dest = current
        while True:
            if (dest := dest - 1) < mn:
                dest = mx
            if dest not in pickup:
                break

        cups[current] = cups[pickup[-1]]
        cups[pickup[-1]] = cups[dest]
        cups[dest] = pickup[0]
        current = cups[current]

    o = ""
    start = cups[1]
    for i in range(l-1):
        o += str(start)
        start = cups[start]
    return o

def solve_b(inp=input_data):
    cupsl = [int(x) for x in inp]
    cupsl += list(range(len(cupsl)+1, 1000001))
    l = 1000000
    cups = {}
    for i in range(l):
        cups[cupsl[i]] = cupsl[(i+1) % l]

    current = cupsl[0]
    mn, mx = 1, 1000000
    for _ in range(10000000):
        pickup = [cups[current]]
        for i in range(2):
            pickup.append(cups[pickup[i]])

        dest = current
        while True:
            if (dest := dest - 1) < mn:
                dest = mx
            if dest not in pickup:
                break

        cups[current] = cups[pickup[-1]]
        cups[pickup[-1]] = cups[dest]
        cups[dest] = pickup[0]
        current = cups[current]

    return cups[1] * cups[cups[1]]

tests = {
"389125467" : ("67384529", 149245887792)
}


# a = solve_a()
# print(f"Part 1: {a}\n")
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



t1 = time.time_ns()
for i in range(times := 1):
    solve_b()
t2 = time.time_ns()
print(f"Part 2: {(t2-t1)/(1000000*times)} ms")