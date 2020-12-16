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

day = 16
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
    rules_, yt, nt = inp.split("\n\n")
    nt = nt.split("\n")[1:]
    yt = yt.split("\n")[1:]
    rules_ = rules_.split("\n")
    rules = {}
    for r in rules_:
        k, v = r.split(": ")
        rules[k] = [tuple(int(x) for x in i.split("-")) for i in v.split(" or ")]

    c = 0
    for t in nt:
        vals = [int(x) for x in t.split(",")]
        for v in vals:
            if not any(s <= v <= e for s,e in sum(rules.values(), [])):
                c += v
    return c

def solve_b(inp=input_data):
    rules_, yt, nt = inp.split("\n\n")
    nt = nt.split("\n")[1:]
    yt = yt.split("\n")[1:]
    rules_ = rules_.split("\n")
    rules = {}
    for r in rules_:
        k, v = r.split(": ")
        rules[k] = [tuple(int(x) for x in i.split("-")) for i in v.split(" or ")]

    c = 0
    valid_t = []
    for t in nt:
        vals = [int(x) for x in t.split(",")]
        if all(any(s <= v <= e for s,e in sum(rules.values(), [])) for v in vals):
            valid_t.append(vals)

    order = collections.defaultdict(list)
    for field, r in rules.items():
        for col in range(len(valid_t[0])):
            col_vals = sum(([t[col]] for t in valid_t), [])
            sat = lambda x: any(s <= x <= e for s,e in r)
            if all(sat(v) for v in col_vals):
                order[field].append(col)

    mapping = {}
    while len(order):
        singles = {k: v[0] for k,v in order.items() if len(v) == 1}
        mapping.update(singles)
        for s in singles.values():
            for k,v in order.copy().items():
                if len(v) <= 1:
                    del order[k]
                elif s in v:
                    order[k].remove(s)

    yt = [int(x) for x in yt[0].split(",")]

    return prod(yt[v] for k,v in mapping.items() if k.startswith("departure"))

tests = {
# """class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12""": (71 ,),
"""class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""": []
}


# a = solve_a()
# print(f"Part 1: {a}\n")
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
# for i in range(times := 1):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")