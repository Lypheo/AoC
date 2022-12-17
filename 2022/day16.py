import time
import functools, collections, re

import networkx as nx
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
import sys
sys.path.append("..")
from aocl import *

day = 16
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = inp.splitlines()
    frs = {}
    ds = {}
    G = nx.Graph()
    for line in inp:
        v = line[6:][:2]
        dst = line.split("to valves ")[1].split(", ") if "valves" in line else line.split("to valve ")[1].split(", ")
        fr = int(line.split("flow rate=")[1].split(";")[0])
        frs[v] = fr
        for d in dst:
            G.add_edge(v, d)
        ds[v] = dst

    nonzero = [v for v, fr in frs.items() if fr]

    @functools.cache
    def val(node, open, time):
        if len(open) == len(nonzero) or time <= 0:
            return 0
        children = ds[node]
        rs = []
        if node not in open and frs[node]:
            newopen = frozenset.union(open, {node})
            rs.append((time-1) * frs[node] + max(val(child, newopen, time - 2) for child in children))
        rs.append(max(val(child, open, time - 1) for child in children))
        return max(rs)
    return val("AA", frozenset(), 30)

def solve_b(inp=input_data):
    # takes literally forever but works lmao
    inp = inp.splitlines()
    flowrates = {}
    G = nx.Graph()
    for line in inp:
        v = line[6:][:2]
        dst = line.split("to valves ")[1].split(", ") if "valves" in line else line.split("to valve ")[1].split(", ")
        fr = int(line.split("flow rate=")[1].split(";")[0])
        flowrates[v] = fr
        for d in dst:
            G.add_edge(v, d)

    weights = {}
    for n1, n2 in combinations(G.nodes(), 2):
        if flowrates[n1] and flowrates[n2] or "AA" in [n1, n2]:
            weights[(n1, n2)] = weights[(n2, n1)] = nx.shortest_path_length(G, n1, n2)
    nonzero = set(v for v, fr in flowrates.items() if fr)

    def val(nodes, open, times):
        if len(open) == len(nonzero):
            return 0

        rs1, rs2 = [], []
        for node, rs, time in zip(nodes, [rs1, rs2], times):
            if time <= 2:
                continue
            for next_node in nonzero - {node} - open:
                newt = time - weights[(node, next_node)] - 1
                rs.append([newt * flowrates[next_node], next_node, open | {next_node}, newt])

        rs1 = rs1 or [[0, "", set(), 0]]
        rs2 = rs2 or [[0, "", set(), 0]]
        M = 0
        i = 0
        for [p1, node1, open1, time1], [p2, node2, open2, time2] in product(rs1, rs2):
            if times[0] == 26: print(i := i +1) # progress
            if node1 == node2:
                continue
            M = max(M, p1 + p2 + val((node1, node2), open1 | open2, (time1, time2)))
        return M

    return val(("AA", "AA"), frozenset(), (26, 26))


tests = {
    """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""" : [1651, 1707]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)
#
test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")