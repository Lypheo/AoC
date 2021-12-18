import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 15
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

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
    inp = [[int(n) for n in x] for x in inp.splitlines()]

    l = len(inp)
    def adjacent(x,y):
        adj = []
        if x > 0:
            adj.append((x-1,y))
        if y > 0:
            adj.append((x,y-1))
        if y < len(inp)-1:
            adj.append((x,y+1))
        if x < len(inp[0])-1:
            adj.append((x+1,y))
        return adj

    import networkx as nx
    G = nx.DiGraph()
    for x,y in itertools.product(range(l), range(l)):
        for xx, yy in adjacent(x,y):
            G.add_edge((x,y), (xx,yy), weight=inp[yy][xx])
    path = nx.dijkstra_path(G, (0,0), (l-1, l-1))
    return sum(inp[y][x] for x,y in path) - inp[0][0]


def solve_b(inp=input_data):
    inp = [[int(n) for n in x] for x in inp.splitlines()]
    l = len(inp)

    def adjacent(x,y):
        adj = []
        if x > 0:
            adj.append((x-1,y))
        if y > 0:
            adj.append((x,y-1))
        if y < len(inp)*5-1:
            adj.append((x,y+1))
        if x < len(inp[0])*5-1:
            adj.append((x+1,y))
        return adj

    import networkx as nx
    G = nx.DiGraph()
    W = {}
    for y in range(l*5):
        for x in range(l*5):
            a, xm = divmod(x, l)
            b, ym = divmod(y, l)
            w = inp[ym][xm]
            for i in range(a+b):
                w = w+1 if w < 9 else 1

            W[(x, y)] = w
    for x,y in itertools.product(range(l*5), range(l*5)):
        for xx, yy in adjacent(x,y):
            G.add_edge((x,y), (xx,yy), weight=W[(xx, yy)])

    path = nx.dijkstra_path(G, (0,0), (l*5-1, l*5-1))
    return sum(W[(x,y)] for x,y in path) - inp[0][0]

tests = {"""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""" : [40, 315]
}

test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)
#
test(tests, solve_b, 1)
# b = solve_b()
# if b:
#     print(f"Part 2: {b}")
#     submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")