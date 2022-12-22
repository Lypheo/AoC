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
day = 22
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    # inp = inp.splitlines()
    map, pathr = inp.split("\n\n")
    grid = {}
    for y, row in enumerate(map.split("\n")):
        for x, tile in enumerate(row):
            if tile == " ":
                continue
            grid[complex(x, y)] = tile

    path = []
    i = 0
    while i < len(pathr):
        if pathr[i:i+2].isnumeric():
            path.append(int(pathr[i:i+2]))
            i += 2
        else:
            t = pathr[i:i+1]

            path.append(t if not t.isnumeric() else int(t))
            i += 1

    dir = complex(1, 0)
    pos = complex(min(c.real for (c, tile) in grid.items() if c.imag == 0), 0)
    rots = {"R": 1j, "L": -1j}
    for ins in path:
        # print(dir, pos, ins)
        if isinstance(ins, int):
            for i in range(ins):
                if pos + dir not in grid:
                    if dir == 1:
                        newpos = min(c.real for (c, tile) in grid.items() if c.imag == pos.imag) + pos.imag * 1j
                    elif dir == -1:
                        newpos = max(c.real for (c, tile) in grid.items() if c.imag == pos.imag) + pos.imag * 1j
                    elif dir == 1j:
                        newpos = min(c.imag for (c, tile) in grid.items() if c.real == pos.real)  * 1j + pos.real
                    else:
                        newpos = max(c.imag for (c, tile) in grid.items() if c.real == pos.real)  * 1j + pos.real
                    if grid[newpos] == "#":
                        break
                    else:
                        pos = newpos
                elif grid[pos + dir] == "#":
                    break
                else:
                    pos += dir
        else:
            dir *= rots[ins]

    return (pos.real + 1) * 4 + (pos.imag + 1) * 1000 + {complex(1, 0): 0, complex(0, -1): 1, complex(-1, 0): 2, complex(0, 1): 3}[dir]

def solve_b(inp=input_data):
    map, pathr = inp.split("\n\n")
    grid = {}
    for y, row in enumerate(map.split("\n")):
        for x, tile in enumerate(row):
            if tile == " ":
                continue
            grid[complex(x, y)] = tile

    path = []
    for (n, r) in re.findall("(\d+)([LR]?)", pathr):
        path.append(int(n))
        if r:
            path.append(r)

    dir = complex(1, 0)
    pos = complex(min(c.real for (c, tile) in grid.items() if c.imag == 0 and tile != "#"), 0)
    rots = {"R": 1j, "L": -1j}
    # sameside = lambda p1, p2: p1.real // 50 == p2.real // 50 and p1.imag // 50 == p2.imag // 50

    htr, vtr = {}, {}
    htr.update({p1: (p2, 1) for p1, p2 in zip(ip(50, 50 + 49j), ip(149j, 100j))})
    htr.update({p2: (p1, 1) for p1, p2 in zip(ip(50, 50 + 49j), ip(149j, 100j))})

    vtr.update({p1: (p2, 1) for p1, p2 in zip(ip(50, 99), ip(150j, 199j))})
    htr.update({p2: (p1, 1j) for p1, p2 in zip(ip(50, 99), ip(150j, 199j))})

    vtr.update({p1: (p2, -1j) for p1, p2 in zip(ip(100, 149), ip(199j, 199j + 49))})
    vtr.update({p2: (p1, 1j) for p1, p2 in zip(ip(100, 149), ip(199j, 199j + 49))})

    htr.update({p1: (p2, -1) for p1, p2 in zip(ip(149, 149+ 49j), ip(99 + 149j, 99 + 100j))})
    htr.update({p2: (p1, -1) for p1, p2 in zip(ip(149, 149+ 49j), ip(99 + 149j, 99 + 100j))})

    vtr.update({p1: (p2, -1) for p1, p2 in zip(ip(100+49j, 149+ 49j), ip(99 + 50j, 99 + 99j))})
    htr.update({p2: (p1, -1j) for p1, p2 in zip(ip(100+49j, 149+ 49j), ip(99 + 50j, 99 + 99j))})

    htr.update({p1: (p2, 1j) for p1, p2 in zip(ip(50+50j, 50+99j), ip(0 + 100j, 49 + 100j))})
    vtr.update({p2: (p1, 1) for p1, p2 in zip(ip(50+50j, 50+99j), ip(0 + 100j, 49 + 100j))})

    vtr.update({p1: (p2, -1) for p1, p2 in zip(ip(50+149j, 99+149j), ip(49 + 150j, 49 + 199j))})
    htr.update({p2: (p1, -1j) for p1, p2 in zip(ip(50+149j, 99+149j), ip(49 + 150j, 49 + 199j))})

    for ins in path:
        if isinstance(ins, int):
            for _ in range(ins):
                if pos + dir not in grid:
                    newpos, newdir = (vtr if dir.imag else htr)[pos]
                    if grid[newpos] == "#":
                        break
                    else:
                        pos = newpos
                        dir = newdir
                elif grid[pos + dir] == "#":
                    break
                else:
                    pos += dir
        else:
            dir *= rots[ins]
    return (pos.real + 1) * 4 + (pos.imag + 1) * 1000 + {complex(1, 0): 0, complex(0, 1): 1, complex(-1, 0): 2, complex(0, -1): 3}[dir]

tests = {
    """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""" : [6032]
}

# test(tests, solve_a, 0)
# a = solve_a(input_data4)
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

# test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
# print(solve_b())
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")