import time
from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

import random as rand

day = 10
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
    adapters = sorted(int(x) for x in inp.split("\n"))
    ones, threes = 1 if adapters[0] == 1 else 0, 1
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1

    return ones * threes


def solve_b(inp=input_data):
    from collections import defaultdict
    c = defaultdict(list)
    adapters = [0] + sorted(int(x) for x in inp.split("\n"))
    adapters.append(max(adapters) + 3)

    for i in range(len(adapters)):
        for k in adapters[i+1:i+4]:
            if k - adapters[i] <= 3:
                c[adapters[i]].append(k)

    @functools.lru_cache(None)
    def f(n):
        if n == adapters[-1]:
            return 1
        return sum(f(k) for k in c[n])

    return f(0)


tests = {"""16
10
15
5
1
11
7
19
6
12
4""" : (8,)
    ,
"""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""": (10*22,19208)
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
# for i in range(times := 10000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")