import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 11
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

def adjacent(xx, yy, inp):
    adj = []
    for x, y in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if xx+x < 0 or xx+x >= len(inp[0]) or yy+y < 0 or yy+y >= len(inp) or (x == 0 and y == 0):
            continue
        adj.append((xx+x, yy+y))
    return adj

def solve_a(inp=input_data):
    octopi = [[int(x) for x in n] for n in inp.splitlines()]
    s = 0

    for i in range(100):
        flashed = set()
        def inc(x,y):
            octopi[y][x] += 1
            if octopi[y][x] > 9 and (x,y) not in flashed:
                flashed.add((x,y))
                for xx, yy in adjacent(x, y, octopi):
                    inc(xx,yy)

        for y,row in enumerate(octopi):
            for x,_ in enumerate(row):
                inc(x,y)

        for y,row in enumerate(octopi):
            for x,_ in enumerate(row):
                octopi[y][x] = octopi[y][x] if octopi[y][x] <= 9 else 0
        s += len(flashed)

    return s

def solve_b(inp=input_data):
    octopi = [[int(x) for x in n] for n in inp.splitlines()]
    l = len(octopi) * len(octopi[0])
    for i in itertools.count():
        flashed = set()
        def inc(x,y):
            octopi[y][x] += 1
            if octopi[y][x] > 9 and (x,y) not in flashed:
                flashed.add((x,y))
                for xx, yy in adjacent(x, y, octopi):
                    inc(xx,yy)

        for y,row in enumerate(octopi):
            for x,_ in enumerate(row):
                inc(x,y)

        for y,row in enumerate(octopi):
            for x,_ in enumerate(row):
                octopi[y][x] = octopi[y][x] if octopi[y][x] <= 9 else 0

        if len(flashed) == l:
            return i+1

tests = {
    """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""" : [1656, 195]
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
# #
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")