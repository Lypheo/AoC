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
from matplotlib import pyplot as plot
import iplotx as ipx


st=time.time()

puzzle = Puzzle(year=2025, day=11)
inp = puzzle.input_data

inp = lines(inp)
p1, p2 = 0, 0
devices = []
G = nx.DiGraph()
for line in inp:
    device, targets = line.split(":")
    targets = targets.strip().split()
    G.add_edges_from((device, target) for target in targets)

# ipx.network(G, nx.layout.bfs_layout(G, "svr"), vertex_labels={k: k if k in ["svr", "dac", "fft", "out", "you"] else "" for k in G.nodes})
# plot.show()

bfslayers = nx.bfs_layers(G, "svr")

def num_paths_between(start, dest, layers=bfslayers):
    """Relies on the fact that the dest layer doesn't have any interconnects or any incoming connections from the next layer"""
    dst_layer = next(layer for layer in layers if dest in layer)
    num_paths = 0
    frontier = {start: 1}
    while frontier:
        newfrontier = dd(int)
        for node, num in frontier.items():
            for conNode in G[node]:
                if conNode in dst_layer:
                    if conNode == dest:
                        num_paths += num
                    continue
                newfrontier[conNode] += num
        frontier = newfrontier
    return num_paths

p1 = num_paths_between("you", "out", nx.bfs_layers(G, "you"))
p2 = num_paths_between("svr", "fft") * num_paths_between("fft", "dac") * num_paths_between("dac", "out")
print(f"Solution: {p1}, {p2}\n")
copy(p2)

print(f"----{(time.time()-st):.3f} s----")