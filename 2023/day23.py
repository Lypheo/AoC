import time
import functools, itertools, collections, re

import networkx as nx
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import matplotlib.pyplot as plt
import sys
sys.path.append("..")
from aocl import *
sys.setrecursionlimit(100000000)
day = 23
puzzle = Puzzle(year=2023, day=day)
inp = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
""".strip()
inp = puzzle.input_data

inp = lines(inp)
res = 0
grid = parse_grid(inp)
start = pos = 1
goal = len(inp) * 1j + len(inp[0]) - 1 - (1+1j)
ds = {"^": -1j, "v": 1j, ">": 1, "<": -1}

CG = nx.Graph()
seen = {(start, start + 1j)}
def f(pos, path):
    nxt = [pos]
    while len(nxt) == 1:
        pos = nxt.pop()
        seen.add((path[-1], pos))
        path = (*path, pos)
        for n in nb(pos):
            if n not in path and n in grid and grid[n] != "#":
                nxt.append(n)
    if not nxt and pos != goal:
        return
    CG.add_edge(path[0], pos, weight=len(path)-1)
    for n in nxt:
        if (pos, n) not in seen:
            f(n, (pos,))

f(start+1j, (start,))
# nx.draw(CG)
# plt.show()
res = list(((nx.path_weight(CG, path, "weight"), path) for path in nx.all_simple_paths(CG, start, goal)))
res = max(res)


# Q = {(pos, (pos,))}
# steps = 0
# stepcs = []
# mem = {}
# while Q:
#     nxt = set()
#     for p, path in Q:
#         if p == goal:
#             stepcs.append(steps)
#             continue
#         for n in nb(p):
#             if n not in path and n in grid and grid[n] != "#":
#                 if n in mem and mem[n] > steps:
#                     continue
#                 else:
#                     nxt.add((n, (*path, n)))
#                     mem[n] = steps
#     Q = nxt
#     steps += 1
#     # print(steps)

# res = max(stepcs)

# def f(pos, path):
#     nxt = [pos]
#     while len(nxt) == 1:
#         pos = nxt.pop()
#         path = (*path, pos)
#         for n in nb(pos):
#             if n not in path and n in grid and grid[n] != "#":
#                 nxt.append(n)
#     # print(pos, path, nxt)
#     if not nxt:
#         out = 0 if pos != goal else len(path)-1
#     else:
#         out = max(f(p, path) for p in nxt)
#     return out
#
# res = f(start, tuple())

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")