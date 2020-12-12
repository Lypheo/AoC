import time
from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 11
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

import copy
dirs = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

def solve_a(inp=input_data):
    grid = [list(x) for x in inp.split("\n")]
    while True:
        newgrid = copy.deepcopy(grid)
        for x, y in itertools.product(range(len(grid[0])), range(len(grid))):
            inbound = lambda x, y: (0 <= x < len(grid[0])) and (0 <= y < len(grid))
            adjacent = sum(grid[y+yp][x+xp] == "#" for xp, yp in dirs if inbound(x+xp, y+yp))
            if grid[y][x] == "#" and adjacent >= 4:
                newgrid[y][x] = "L"
            elif grid[y][x] == "L" and adjacent == 0:
                newgrid[y][x] = "#"

        if grid == newgrid:
            return sum(row.count("#") for row in newgrid)
        grid = newgrid

def solve_b(inp=input_data):
    grid = [list(x) for x in inp.split("\n")]
    while True:
        newgrid = copy.deepcopy(grid)
        for x, y in itertools.product(range(len(grid[0])), range(len(grid))):
            inbound = lambda x, y: (0 <= x < len(grid[0])) and (0 <= y < len(grid))
            adjacent = 0
            for do in dirs:
                d = do
                while inbound(x + d[0], y + d[1]):
                    seat = grid[y + d[1]][x + d[0]]
                    if seat == "#":
                        adjacent += 1
                        break
                    elif seat == "L":
                        break
                    d = (d[0]+do[0], d[1]+do[1])

            if grid[y][x] == "#" and adjacent >= 5:
                newgrid[y][x] = "L"
            elif grid[y][x] == "L" and adjacent == 0:
                newgrid[y][x] = "#"

        if grid == newgrid:
            return sum(row.count("#") for row in newgrid)
        grid = newgrid

tests = {
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""": (37, 26)
}


# a = solve_a()
# print(f"Part 1: {a}\n")
test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

# b = solve_b()
# print(f"Part 2: {b}")
test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")
#
t1 = time.time_ns()
for i in range(times := 5):
    solve_b()
t2 = time.time_ns()
print(f"Part 2: {(t2-t1)/(1000000*times)} ms")