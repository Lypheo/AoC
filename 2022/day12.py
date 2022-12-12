import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 12
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data
import networkx as nx

def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    inp = inp.splitlines()
    grid = {}
    G = nx.DiGraph()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            h = inp[y][x]
            if h == "E":
                goal = x + y*1j
            elif h == "S":
                start = x + y*1j
            grid[x + y*1j] = {"S": 0, "E": 25}.get(h, ord(h)-ord("a"))
    for k,v in grid.items():
        for i in range(4):
            adj = k+1j**i
            if grid.get(adj, 100) <= v + 1:
                G.add_edge(k, adj)

    return nx.shortest_path_length(G,source=start,target=goal)

def solve_b(inp=input_data):
    inp = inp.splitlines()
    grid = {}
    G = nx.DiGraph()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            h = inp[y][x]
            if h == "E":
                goal = x + y*1j
            grid[x + y*1j] = {"S": 0, "E": 25}.get(h, ord(h)-ord("a"))
    for k,v in grid.items():
        for i in range(4):
            adj = k+1j**i
            if grid.get(adj, 100) <= v + 1:
                G.add_edge(k, adj)
    starts = [k for k,v in grid.items() if v == 0]
    return min(nx.shortest_path_length(G,source=s,target=goal) for s in starts if nx.has_path(G, source=s, target=goal))

tests = {
    """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""": [31, 29]
}

test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)
#
test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")