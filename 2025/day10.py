import os
import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from aocl import *
from functional import seq
from fn import _ as l
from pyperclip import copy
import networkx as nx

st=time.time()

puzzle = Puzzle(year=2025, day=10)
inp = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()
inp = puzzle.input_data

inp = lines(inp)
machines = []
for line in inp:
    parts = line.split()
    lights = tuple(c == "#" for c in parts[0][1:-1])
    joltage = tuple(ints(parts[-1]))
    buttons = [tuple(ints(btn)) for btn in parts[1:-1]]
    machines.append((lights, buttons, joltage))
res = 0
# probably way overkill since a simple BFS suffices but whatever
for lights, buttons, joltage in machines:
    G = nx.Graph()
    for i in range(2**len(lights)):
        binary = format(i, f"0{len(lights)}b")
        node = tuple(c == "1" for c in binary)
        G.add_node(node)
        for button in buttons:
            target = tuple(not node[j] if j in button else node[j] for j in range(len(node)))
            G.add_edge(node, target)
    start = tuple(False for _ in range(len(lights)))
    res += nx.shortest_path_length(G, start, lights)

print(f"Solution: {res}\n")
copy(res)

print(f"----{(time.time()-st):.3f} s----")