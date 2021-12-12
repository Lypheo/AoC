import pprint

import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 12
puzzle = Puzzle(year=2021, day=day)
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
    inp1 = [p.split("-") for p in inp.splitlines()]
    inp2 = [p.split("-")[::-1] for p in inp.splitlines()]
    cs = dd(list)
    for k,v in inp1: cs[k].append(v)
    for k,v in inp2: cs[k].append(v)

    paths = [["start", n] for n in cs["start"]]
    while any(p[-1] != "end" for p in paths):
        newp = []
        for p in paths:
            last = p[-1]
            visited = [k for k in p if k.islower()]
            if last == "end":
                newp.append(p)
                continue
            nxt = [k for k in cs[last] if k not in visited]
            newp.extend(p + [node] for node in nxt)
        paths = newp


    return len(paths)

def solve_b(inp=input_data):
    inp1 = [p.split("-") for p in inp.splitlines()]
    inp2 = [p.split("-")[::-1] for p in inp.splitlines()]
    cs = dd(list)
    for k,v in inp1: cs[k].append(v)
    for k,v in inp2: cs[k].append(v)

    paths = [["start", n] for n in cs["start"]]
    while any(p[-1] != "end" for p in paths):
        newp = []
        for p in paths:
            last = p[-1]
            cnts = [p.count(k) for k in p if k.islower()]
            visited = [k for k in p if k.islower() and 2 in cnts] + ["start"]

            if last == "end":
                newp.append(p)
                continue
            nxt = [k for k in cs[last] if (k not in visited)]
            newp.extend(p + [node] for node in nxt)
        paths = newp

    return len(paths)
tests = {
    """start-A
start-b
A-c
A-b
b-d
A-end
b-end""" : [10,36]
}

test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

test(tests, solve_b, 1)
# b = solve_b()
# if b:
#     print(f"Part 2: {b}")
#     submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
# #
# import time
# t1 = time.time_ns()
# for i in range(times := 5):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")