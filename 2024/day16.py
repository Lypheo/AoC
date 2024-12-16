import time
import functools, itertools, collections, re

import networkx as nx
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
sys.setrecursionlimit(9999999)
from aocl import *
from functional import seq
from fn import _ as l
from pyperclip import copy
import networkx
st=time.time()

day = 16
puzzle = Puzzle(year=2024, day=day)
inp = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()
inp = puzzle.input_data

grid = parse_grid(inp)
res = 0
pos = grid.keys().seq().find(lambda k: grid[k] == "S")
goal = grid.keys().seq().find(lambda k: grid[k] == "E")
grid[pos] = "."
grid[goal] = "."

G = nx.DiGraph()
seen = set()
def f(p, d):
    if (p, d) in seen:
        return
    seen.add((p, d))
    for n in nbc(p):
        if n == p - d: continue
        if grid[n] == ".":
            G.add_weighted_edges_from([((p, d), (n, n - p), 1 if n == p + d else 1001)])
            f(n, n - p)

f(pos, 1)
minscore = 1e99
for d in nb(0):
    if (goal, d) in G:
        if (length := nx.shortest_path_length(G, source=(pos, 1), target=(goal,d), weight='weight'))  < minscore:
            minscore = length
            sps = nx.all_shortest_paths(G, source=(pos, 1), target=(goal,d), weight='weight').seq().flatten().map(lambda x: x[0]).to_set()
            p2 = len(sps)
            p1 = length

print(f"Solution: {p1, p2}\n")
copy(res)

print("----%.2f s----"%(time.time()-st))
