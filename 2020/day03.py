from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 3
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True


def solve_a(inp=input_data):
    grid = []
    for l in inp.split("\n"):
        grid.append(l)
    c = 0
    i = 0
    while i < len(grid):
        c += int(grid[i][(i*3) % len(grid[0])] == "#")
        i += 1

    return c

def solve_b(inp=input_data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    grid = inp.split("\n")
    w, h = len(grid[0]), len(grid)
    o = 1
    for x,y in slopes:
        o *= sum(grid[ey][(ex) % w] == "#" for ex,ey in zip(itertools.count(0, x), range(0, h, y)))
    return o

tests = {
"""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""" : (7, 336)
}

a = solve_a()
print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

b = solve_b()
if not b:
    exit(0)

print(f"Part 2: {b}")
# test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

import time
t1 = time.time_ns()
for i in range(times := 1000):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")