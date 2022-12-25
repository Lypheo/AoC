import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
import sys
sys.path.append("..")
from aocl import *
day = 24
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = inp.splitlines()
    sgrid = dict()
    for y, row in enumerate(inp):
        for x, tile in enumerate(row):
            if tile == ".":
                continue
            sgrid[complex(x, y)] = [tile]
    maxx = int(max(c.real for c in sgrid.keys()))
    maxy = int(max(c.imag for c in sgrid.keys()))
    start = next(x for x in range(maxx) if x not in sgrid)
    end = next(x for x in range(maxx) if maxy*1j + x not in sgrid) + maxy*1j
    sgrid[start - 1j] = "#"
    print(start, end)
    dirs = {">": complex(1, 0), "v": complex(0, 1), "<": complex(-1, 0), "^": complex(0, -1)}
    grid = sgrid
    states = {start}
    for i in count(1):
        nextstates = set()
        nextg = dd(list)
        for pos, tiles in grid.items():
            for tile in tiles:
                if tile in dirs.keys():
                    nextpos = pos + dirs[tile]
                    x, y = nextpos.real, nextpos.imag
                    if x == 0:
                        x = maxx-1
                    elif x == maxx:
                        x = 1
                    elif y == 0:
                        y = maxy-1
                    elif y == maxy:
                        y = 1
                    nextg[x + y*1j].append(tile)
                else:
                    nextg[pos] = [tile]
        for cpos in states:
            nextcpos = [cpos + c for c in dirs.values() if cpos + c not in nextg]
            if cpos not in nextg:
                nextcpos.append(cpos)
            if end in nextcpos:
                return i
            nextstates.update(nextcpos)

        print(i, len(nextstates))
        states = nextstates
        grid = nextg
    return None

def solve_b(inp=input_data):
    inp = inp.splitlines()
    sgrid = dict()
    for y, row in enumerate(inp):
        for x, tile in enumerate(row):
            if tile == ".":
                continue
            sgrid[complex(x, y)] = [tile]
    maxx = int(max(c.real for c in sgrid.keys()))
    maxy = int(max(c.imag for c in sgrid.keys()))
    start = next(x for x in range(maxx) if x not in sgrid)
    end = next(x for x in range(maxx) if maxy*1j + x not in sgrid) + maxy*1j
    sgrid[start - 1j] = "#"
    sgrid[end + 1j] = "#"
    print(start, end)
    dirs = {">": complex(1, 0), "v": complex(0, 1), "<": complex(-1, 0), "^": complex(0, -1)}
    grid = sgrid
    states = {start}
    goal = [end, start, end]
    for i in count(1):
        nextstates = set()
        nextg = dd(list)
        for pos, tiles in grid.items():
            for tile in tiles:
                if tile in dirs.keys():
                    nextpos = pos + dirs[tile]
                    x, y = nextpos.real, nextpos.imag
                    if x == 0:
                        x = maxx-1
                    elif x == maxx:
                        x = 1
                    elif y == 0:
                        y = maxy-1
                    elif y == maxy:
                        y = 1
                    nextg[x + y*1j].append(tile)
                else:
                    nextg[pos] = [tile]
        for cpos in states:
            nextcpos = [cpos + c for c in dirs.values() if cpos + c not in nextg]
            if cpos not in nextg:
                nextcpos.append(cpos)
            if goal[0] in nextcpos:
                nextstates = {goal.pop(0)}
                if not goal:
                    return i
                break
            nextstates.update(nextcpos)

        print(i, len(nextstates))
        states = nextstates
        grid = nextg
    return None

tests = {
    """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""" : [18, 54]
}

test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")