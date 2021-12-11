import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 9
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data
# input_data = open(r"C:\Users\saifu\Downloads\9-4096-4.in").read().strip()

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
    inp = [[int(x) for x in n] for n in inp.splitlines()]
    # print(inp)
    s = 0
    for y, row in enumerate(inp):
        for x,e in enumerate(row):
            adj = []
            if x > 0:
                adj.append(inp[y][x-1])
            if y > 0:
                adj.append(inp[y-1][x])
            if y < len(inp)-1:
                adj.append(inp[y+1][x])
            if x < len(inp[0])-1:
                adj.append(inp[y][x+1])
            if all(e < k for k in adj):
                print(x, y, e, adj)
                s += 1+e
    return s

def solve_b(inp=input_data):
    inp = [[int(x) for x in n] for n in inp.splitlines()]
    basins = []
    def adjacent(x,y):
        adj = []
        if x > 0:
            adj.append((x-1,y))
        if y > 0:
            adj.append((x,y-1))
        if y < len(inp)-1:
            adj.append((x,y+1))
        if x < len(inp[0])-1:
            adj.append((x+1,y))
        return adj

    flow = dd(set)
    low = []
    for y, row in enumerate(inp):
        for x,e in enumerate(row):
            if e == 9:
                continue
            adj = adjacent(x, y)
            flow[min(adj + [(x,y)], key = lambda p: inp[p[1]][p[0]])].add((x,y))
            if all(e < k for k in [inp[p[1]][p[0]] for p in adj]):
                low.append((x,y))

    for x,y in low:
        basin = {(x, y)}
        while True:
            newb = basin.copy()
            for x,y in basin:
                newb.update(flow[(x,y)])
            if len(newb) == len(basin):
                break
            basin = newb
        basins.append(basin)
    from numpy import prod
    return prod(sorted(map(len, basins))[-3:])

tests = {
    """2199943210
3987894921
9856789892
8767896789
9899965678""" : [15, 1134]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)
#
# test(tests, solve_b, 1)
b = solve_b()
if b:
    print(f"Part 2: {b}")
    # submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")