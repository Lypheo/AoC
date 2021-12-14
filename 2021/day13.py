import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 13
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
    cs, ins = inp.split("\n\n")
    cs = [[int(x) for x in k.split(",")] for k in cs.split("\n")]
    ins = [(k.split("=")[0][-1], int(k.split("=")[1])) for k in ins.split("\n")]
    grid = {(x,y) for x,y in cs}
    for dir, c in ins[0:1]:
        newg = set()
        if dir == "x":
            for x,y in grid:
                if x > c:
                    newg.add((c-(x-c), y))
                else:
                    newg.add((x, y))
        grid = newg
    return len(grid)

def solve_b(inp=input_data):
    cs, ins = inp.split("\n\n")
    cs = [[int(x) for x in k.split(",")] for k in cs.split("\n")]
    ins = [(k.split("=")[0][-1], int(k.split("=")[1])) for k in ins.split("\n")]
    grid = {cs}
    for dir, c in ins:
        newg = set()
        if dir == "x":
            for x,y in grid:
                if x > c:
                    newg.add((c-(x-c), y))
                else:
                    newg.add((x, y))
        else:
            for x,y in grid:
                if y > c:
                    newg.add((x, c-(y-c)))
                else:
                    newg.add((x, y))
        grid = newg

    y = [y for x,y in grid]
    x = [x for x,y in grid]
    miny, maxy, minx, maxx = min(y), max(y), min(x), max(x)
    s = ""
    for yi in range(miny, maxy+1):
        for xi in range(minx, maxx+1):
            s += "#" if (xi,yi) in grid else " "
        s += "\n"

    return s
#
tests = {
    """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""" : [17, -1]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

# test(tests, solve_b, 1)
b = solve_b()
if b:
    print(f"Part 2: {b}")
#     submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
# #
import time
t1 = time.time_ns()
for i in range(times := 1000):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(times)} ns")