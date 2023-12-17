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
day = 16
puzzle = Puzzle(year=2023, day=day)
inp = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip()
inp = puzzle.input_data

t1 = time.time_ns()
grid = parse_grid(lines(inp))
minx, maxx = min([p.real for p in grid.keys()]), max([p.real for p in grid.keys()])
miny, maxy = min([p.imag for p in grid.keys()]), max([p.imag for p in grid.keys()])
within_bounds = lambda p: minx <= p.real <= maxx and miny <= p.imag <= maxy
res = 0
configs = []
for x in sri(minx, maxx): configs.append({x: "v"})
for x in sri(minx, maxx): configs.append({x + maxy * 1j: "^"})
for y in sri(miny, maxy): configs.append({y * 1j: ">"})
for y in sri(miny, maxy): configs.append({y * 1j + maxx: "<"})

for arrows in configs:
    energized = set()
    seen = set()
    while True:
        arrowt = tuple(sorted([(p, v) for p,v in arrows.items()], key=lambda t: t[0].real + t[0].imag * 12000))
        if not arrowt in seen:
            seen.add(arrowt)
        else:
            break
        # print(arrows, len(energized))
        newarrows = {}
        for p, v in arrows.items():
            assert v in ("<", ">", "^", "v")

            d = {"<": -1, ">": 1, "^":-1j, "v":1j}[v]
            for i in count(0):
                newp = p + d * i
                if newp not in grid:
                    break
                energized.add(newp)
                if grid[newp] == ".":
                    continue
                if v in ("<", ">"):
                    if grid[newp] == "-":
                        continue
                    elif grid[newp] == "|":
                        if within_bounds(newp + 1j): newarrows[newp + 1j] = "v"
                        if within_bounds(newp - 1j): newarrows[newp - 1j] = "^"
                    elif grid[newp] == "\\":
                        if v == "<":
                            if within_bounds(newp - 1j): newarrows[newp - 1j] = "^"
                        elif v == ">":
                            if within_bounds(newp + 1j): newarrows[newp + 1j] = "v"
                    elif grid[newp] == "/":
                        if v == "<":
                            if within_bounds(newp + 1j): newarrows[newp + 1j] = "v"
                        elif v == ">":
                            if within_bounds(newp - 1j): newarrows[newp - 1j] = "^"
                    break
                elif v in ("^", "v"):
                    if grid[newp] == "|":
                        continue
                    elif grid[newp] == "-":
                        if within_bounds(newp - 1): newarrows[newp - 1] = "<"
                        if within_bounds(newp + 1): newarrows[newp + 1] = ">"
                        break
                    elif grid[newp] == "\\":
                        if v == "^":
                            if within_bounds(newp - 1): newarrows[newp - 1] = "<"
                        elif v == "v":
                            if within_bounds(newp + 1): newarrows[newp + 1] = ">"
                    elif grid[newp] == "/":
                        if v == "^":
                            if within_bounds(newp + 1): newarrows[newp + 1] = ">"
                        elif v == "v":
                            if within_bounds(newp - 1): newarrows[newp - 1] = "<"
                    break
        arrows = newarrows
    res = max(res, len(energized))

print(f"Solution: {res}\n")
# submit(res)

# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1) / 1000000} ms")