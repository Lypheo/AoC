import time
import functools, itertools, collections, re
from tqdm import tqdm
import networkx as nx
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
from aocl import *
from functional import seq
from fn import _ as l
from pyperclip import copy

st=time.time()

puzzle = Puzzle(year=2024, day=20)
inp = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()
inp = puzzle.input_data

grid = parse_grid(inp)
pos = grid.keys().seq().find(lambda k: grid[k] == "S")
goal = grid.keys().seq().find(lambda k: grid[k] == "E")
grid[pos] = "."
grid[goal] = "."

G = nx.Graph()
for p in grid:
    if grid[p] != ".": continue
    for n in nbc(p):
        if grid[n] == ".":
            G.add_edge(p, n)

naive_path = nx.shortest_path(G, pos, goal)
naive = len(naive_path)
paths_goal = nx.shortest_path_length(G, goal)

def solve(cheat_duration):
    res = 0
    for i, p in enumerate(naive_path[:-1]):
        ns = [n for n in naive_path[i+2:] if mh_dist(p, n) <= cheat_duration]
        for end in ns:
            td = naive - (i + paths_goal[end] + mh_dist(p, end))
            if td >= 100:
                res += 1
    return res

print(f"Solution: {solve(2), solve(20)}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")