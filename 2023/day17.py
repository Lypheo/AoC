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
from aocl import *
day = 17
puzzle = Puzzle(year=2023, day=day)
inp = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".strip()
inp = puzzle.input_data

sys.setrecursionlimit(100000)
infty = 9999999999999999
inp = lines(inp)
grid = parse_grid(inp)
grid = {k: int(v) for k,v in grid.items()}
maxx, maxy = max([p.real for p in grid.keys()]), max([p.imag for p in grid.keys()])
goal = maxx + maxy * 1j

def djkstra(straight = False):
    dist = dd(lambda:infty)
    prev = dict()
    q = list(grid.keys())
    dist[0] = 0
    prev[0] = 0
    while q:
        u = min(q, key=lambda x: dist[x])
        q.remove(u)
        d = u - prev[u]
        nb = [u + d*1j, u + d*-1j, u + d] if d else [u + 1, u + 1j]
        if not straight:
            last3 = [prev[u], prev[prev[u]], prev[prev[prev[u]]]]
            if last3 == [u - d, u - 2*d, u - 3*d]:
                nb = nb[:2]
        for v in nb:
            if v not in q:
                continue
            alt = dist[u] + grid[v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev

def get_path(pos, prev):
    path = [pos]
    while pos != 0:
        pos = prev[pos]
        path.append(pos)
    return path

def valid(path):
    for i in range(len(path) - 4):
        ds = [path[i+j] - path[i+j+1] for j in range(4)]
        if len(set(ds)) == 1:
            return False
    return True


dist, prev = djkstra()
maxcost = dist[goal]
print(dist)
# dist2, _  = djkstra(True)
# mincost = dist2[goal]

# path = get_path(goal, prev)
# grid2 = grid.copy()
# for p1, p2 in pairwise(reversed(path)):
#     grid2[p2] = {1: ">", -1: "<", 1j: "v", -1j: "^"}[p2 - p1]
# pgrid(grid2)

DP = {}
@functools.cache
def search(cost, pos, last3):
    if cost > maxcost or pos.real > maxx or pos.imag > maxy or mh_dist(pos, goal)*3 > maxcost - cost:
        return infty
    if pos == goal:
        return cost
    d = pos - last3[0]
    nxt = [pos + d*1j, pos + d*-1j, pos + d] if d else [pos + 1, pos + 1j]
    if last3 == (pos - d, pos - 2*d, pos - 3*d):
        nxt = nxt[:2]
    nxt = [np for np in nxt if np in grid]
    return min(search(cost + grid[np], np, (pos, *last3[:-1])) for np in nxt)

res = search(0, 0, (0, 0, 0))

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")