import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 5
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) != o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True
from collections import defaultdict as dd
def solve_a(inp=input_data):
    inp = [x.split(" -> ") for x in inp.splitlines()]
    lines = []
    for i in inp:
        k = []
        for x in i:
            a,b = x.split(",")
            k.append((int(a), int(b)))
        k = sorted(k, key = lambda p: (p[0]**2 + p[1]**2)**0.5)
        lines.append(tuple(k))

    points = dd(int)
    for l in lines:
        if (l[0][0] != l[1][0] and l[0][1] != l[1][1]): continue
        for x in range(l[0][0], l[1][0]+1):
            for y in range(l[0][1], l[1][1]+1):
                points[(x,y)] += 1

    return sum(v > 1 for k,v in points.items())

def solve_b(inp=input_data):
    inp = [x.split(" -> ") for x in inp.splitlines()]
    lines = []
    for i in inp:
        k = []
        for x in i:
            a,b = x.split(",")
            k.append((int(a), int(b)))
        k = sorted(k, key = lambda p: (p[0]**2 + p[1]**2)**0.5)
        lines.append(tuple(k))

    points = dd(int)
    ps = lambda x1, x2: list(range(x1, x2+1)) if x2 > x1 else list(reversed((range(x2, x1+1))))
    for l in lines:
        x1, y1 = l[0]
        x2, y2 = l[1]
        if (l[0][0] != l[1][0] and l[0][1] != l[1][1]):
            for x,y in zip(ps(x1, x2), ps(y1, y2)):
                points[(x,y)] += 1
        else:
            for x in range(l[0][0], l[1][0]+1):
                for y in range(l[0][1], l[1][1]+1):
                    points[(x,y)] += 1

    return sum(v > 1 for k,v in points.items())

tests_a = {
    """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""" : 5
}

# test(tests_a, solve_a)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(a, part="a", day=day, year=2021)

tests_b = {
    """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""" : 12
}

# test(tests_b, solve_b)
b = solve_b()
if b:
    print(f"Part 2: {b}")
    submit(b, part="b", day=day, year=2021)
