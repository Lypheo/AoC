import copy
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
day = 25
puzzle = Puzzle(year=2023, day=day)
inp = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
""".strip()
inp = puzzle.input_data

inp = lines(inp)
res = 0

edges = []
graph = nx.Graph()
for line in inp:
    a, bs = line.split(": ")
    bs = bs.split(" ")
    for b in bs:
        graph.add_edge(a, b)

for wire in edges:
    # gc = copy.deepcopy(graph)
    graph.remove_edge(*wire)
    if not nx.has_path(graph, wire[0], wire[1]):
        g1 = graph.subgraph([n for n in graph.nodes if nx.has_path(graph, wire[0], n)])
        g2 = graph.subgraph([n for n in graph.nodes if nx.has_path(graph, wire[1], n)])
        res = len(g1.nodes) * len(g2.nodes)

# pathd = nx.shortest_path(graph)
# paths = [vv for k,v in pathd.items() for kk,vv in v.items() if len(vv) > 3]
# nodes = dd(int)
# # print(paths)
# for path in paths:
#     for node in path:
#         nodes[node] += 1
#
# ns = sorted([(v, k) for k,v in nodes.items()], reverse=True)
# for v in combinations([n for _,n in ns], 6):
#     gc = copy.deepcopy(graph)
#     a, b = None, None
#     for wire in combinations(v, 2):
#         if gc.has_edge(*wire):
#             a, b = wire
#             gc.remove_edge(*wire)
#
#     if a and b and not nx.has_path(gc, a, b):
#         g1 = gc.subgraph([n for n in gc.nodes if nx.has_path(gc, a, n)])
#         g2 = gc.subgraph([n for n in gc.nodes if nx.has_path(gc, b, n)])
#         res = len(g1.nodes) * len(g2.nodes)

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")