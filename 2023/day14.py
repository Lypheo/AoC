import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
from aocl import *
day = 14
puzzle = Puzzle(year=2023, day=day)
inp = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip()
inp = puzzle.input_data


# res = 0
# grid = []
# for y, row in enumerate(inp.splitlines()):
#     grid.append([])
#     for x, col in enumerate(row):
#         grid[-1].append(col)
# lenx, leny = len(grid[0]), len(grid)
# print(leny, lenx)
# for x in range(lenx):
#     for y in range(leny):
#         c = grid[y][x]
#         if c == "O":
#             grid[y][x] = "."
#             newy = y
#             while newy >= 1 and grid[newy-1][x] == ".":
#                 newy -= 1
#             grid[newy][x] = "O"
#             res += leny - newy

res = 0
grid = []
for y, row in enumerate(inp.splitlines()):
    grid.append([])
    for x, col in enumerate(row):
        grid[-1].append(col)
lenx, leny = len(grid[0]), len(grid)

def rotate_grid(g): # rotate left
    newg = []
    for y in range(leny):
        newg.append([])
        for x in range(lenx):
            newg[-1].append(g[lenx-x-1][y])
    return newg

loads = []
cycle_length = 0
ans = 0
for cycle in range(1, 1000000000):
    for d in range(4):
        res = 0
        for x in range(lenx):
            for y in range(leny):
                c = grid[y][x]
                if c == "O":
                    grid[y][x] = "."
                    newy = y
                    while newy >= 1 and grid[newy-1][x] == ".":
                        newy -= 1
                    grid[newy][x] = "O"
                    res += lenx - x
        grid = rotate_grid(grid)
    if cycle_length:
        if (cycle % cycle_length) == (1000000000 % cycle_length):
            ans = res
            break

    loads.append(res)
    prev_res = [i for i in range(len(loads)) if loads[i] == res]
    if len(prev_res) > 10: # arbitrary heuristic
        diffs = [prev_res[i] - prev_res[i-1] for i in range(1, len(prev_res))]
        if len(set(diffs[-5:])) == 1:
            cycle_length = diffs[-1]

# print("\n".join("".join(row) for row in grid))
print(f"Solution: {ans}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")