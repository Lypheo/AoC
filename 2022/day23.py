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
day = 23
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = inp.splitlines()
    grid = set()
    for y, row in enumerate(inp):
        for x, tile in enumerate(row):
            if tile =="#":
                grid.add(complex(x, y))

    dirs = [
        [-1j - 1, -1j, -1j + 1],
        [1j - 1, 1j, 1j + 1],
        [1j - 1, -1, -1j - 1],
        [1j + 1, +1, -1j + 1]
    ]
    alladj = set(sum(dirs, []))
    for _ in range(10):
        pgrid(grid, t= "set")
        props = {}
        newgrid = set()
        for e in grid:
            if all(a + e not in grid for a in alladj):
                props[e] = e
                continue
            for adj in dirs:
                if all(a + e not in grid for a in adj):
                    props[e] = e + adj[1]
                    break
            else:
                props[e] = e
        print(props)
        pvs = list(props.values())
        for e, prop in props.items():
            if pvs.count(prop) == 1:
                newgrid.add(prop)
            else:
                newgrid.add(e)
        dirs = dirs[1:] + [dirs[0]]
        grid = newgrid
    x1, x2 = min([p.real for p in grid]), max([p.real for p in grid])
    y1, y2 = min([p.imag for p in grid]), max([p.imag for p in grid])
    x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])
    return sum(1 for x in sr(x1, x2, inc=True) for y in sr(y1, y2, inc=True) if complex(x,y) not in grid)

def solve_b(inp=input_data):
    inp = inp.splitlines()
    grid = set()
    for y, row in enumerate(inp):
        for x, tile in enumerate(row):
            if tile =="#":
                grid.add(complex(x, y))

    dirs = [
        [-1j - 1, -1j, -1j + 1],
        [1j - 1, 1j, 1j + 1],
        [1j - 1, -1, -1j - 1],
        [1j + 1, +1, -1j + 1]
    ]
    alladj = set(sum(dirs, []))
    for _ in count(1):
        # pgrid(grid, t= "set")
        props = {}
        newgrid = set()
        for e in grid:
            if all(a + e not in grid for a in alladj):
                props[e] = e
                continue
            for adj in dirs:
                if all(a + e not in grid for a in adj):
                    props[e] = e + adj[1]
                    break
            else:
                props[e] = e
        # print(props)
        pvs = list(props.values())
        for e, prop in props.items():
            if pvs.count(prop) == 1:
                newgrid.add(prop)
            else:
                newgrid.add(e)
        dirs = dirs[1:] + [dirs[0]]
        if grid == newgrid:
            return _
        grid = newgrid
    x1, x2 = min([p.real for p in grid]), max([p.real for p in grid])
    y1, y2 = min([p.imag for p in grid]), max([p.imag for p in grid])
    x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])
    return sum(1 for x in sr(x1, x2, inc=True) for y in sr(y1, y2, inc=True) if complex(x,y) not in grid)


tests = {
#     """.....
# ..##.
# ..#..
# .....
# ..##.
# .....""": [1],
    """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""" : [110, 20]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)
# #
test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)

#
import time
t1 = time.time_ns()
for i in range(times := 1):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")