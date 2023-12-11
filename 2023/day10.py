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
import networkx as nx
from aocl import *
day = 10
puzzle = Puzzle(year=2023, day=day)
inp = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip()
inp = puzzle.input_data

import time
t1 = time.time_ns()
for i in range(times := 10):
    grid = {}
    start = None
    for y, row in enumerate(lines(inp)):
        for x, col in enumerate(row):
            grid[complex(x, y)] = col
            if col == "S":
                start = complex(x, y)
    assert start
    loop = nx.Graph()
    cur = start
    maxd = 0
    visited = set()
    matches = {-1j: [a + b for b in "|F7" for a in "|JL"],
               1j:[a + b for a in "|F7" for b in "|JL"],
               -1:[a + b for a in "-J7" for b in "-FL"],
               1:[a + b for b in "-J7" for a in "-FL"]}
    def get_links(curr):
        links = []
        for n in nb(0):
            pos = curr + n
            tile = grid.get(pos, ".")
            curtile = grid.get(curr, ".")
            if any(curtile == m[0] and tile == m[1] for m in matches[n]):
                links.append((curr, pos))
        return links

    grid[start] = "|"
    options = ["-","L","J","7","F"]
    while len(get_links(start)) != 2:
        grid[start] = options.pop()

    while True:
        visited.add(cur)
        loop.add_edges_from(get_links(cur))
        nxt = list(x for x in loop.neighbors(cur) if x not in visited)
        if not nxt:
            break
        cur = nxt.pop()

    p1 = max(nx.shortest_path_length(loop, start).values())
    curvature = {}
    pos = min(loop.nodes, key=lambda n: n.real)
    grads = {"|": 1, "L": -1j + 1, "F": 1j + 1, "-": 1j, "J": -1j - 1, "7": 1j - 1}
    curvature[pos] = grads[grid[pos]]
    visited = {pos}
    while len(visited) < len(loop.nodes):
        last = pos
        pos = list(x for x in loop.neighbors(last) if x not in visited).pop()
        visited.add(pos)
        curv = grads[grid[pos]]
        if mh_dist(curv, curvature[last]) >= mh_dist(-curv, curvature[last]) and mh_dist(curv + pos, last + curvature[last]) >= mh_dist(-curv + pos, last + curvature[last]):
            curv *= -1
        curvature[pos] = curv
    # m = {-1: "←", 1:"→", -1j:"↑", 1j:"↓", -1-1j:"↖", 1-1j:"↗", 1+1j:"↘", -1+1j:"↙"}
    # pgrid({k: m[v] for k,v in curvature.items()})

    x1, x2 = min([p.real for p in loop.nodes]), max([p.real for p in loop.nodes])
    y1, y2 = min([p.imag for p in loop.nodes]), max([p.imag for p in loop.nodes])
    part2 = 0
    for x in sri(x1, x2):
        for y in sri(y1, y2):
            p = complex(x, y)
            if p in loop.nodes:
                continue
            enclosed = None
            for d in nb(0):
                for i in count(1):
                    p2 = p + d*i
                    if p2 not in grid:
                        enclosed = False
                        break
                    if p2 not in curvature:
                        continue
                    enclosed = d.real and curvature[p2].real == -d.real or d.imag and curvature[p2].imag == -d.imag
                    break
                if not (enclosed is None):
                    break
            assert not (enclosed is None)
            part2 += int(enclosed)

    print(f"Solution: {part2}\n")

t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")
