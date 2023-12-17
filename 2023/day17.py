import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod, ceil, floor
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
# SCX, SCY = 12, 13
inp = puzzle.input_data
SCX, SCY = 11, 11
MIND, MAXD = 4, 10

sys.setrecursionlimit(100000)
infty = 9999999999999999
inp = lines(inp)
grid = parse_grid(inp)
grid = {k: int(v) for k,v in grid.items()}
maxx, maxy = max([p.real for p in grid.keys()]), max([p.imag for p in grid.keys()])
goal = maxx + maxy * 1j

# def djkstra():
#     dist = dd(lambda:infty)
#     prev = dict()
#     q = list(grid.keys())
#     dist[0] = 0
#     prev[0] = 0
#     while q:
#         u = min(q, key=lambda x: dist[x])
#         if dist[u] == infty:
#             break
#         q.remove(u)
#         d = u - prev[u]
#         if not d: # start
#             nb = [u + 1, u + 1j]
#         else:
#             last = []
#             cur = prev[u]
#             for i in range(MAXD):
#                 last.append(cur)
#                 cur = prev[cur]
#             if last == [u - d*i for i in range(1, MAXD+1)]:
#                 nb = [u + d*1j, u + d*-1j]
#             elif last[:MIND] == [u - d*i for i in range(1, MIND+1)]:
#                 nb = [u + d*1j, u + d*-1j, u + d]
#             else:
#                 nb = [u + d]
#
#         for v in nb:
#             if v not in q:
#                 continue
#             alt = dist[u] + grid[v]
#             if alt < dist[v]:
#                 dist[v] = alt
#                 prev[v] = u
#     return dist, prev
#
# def get_path(pos, prev):
#     path = [pos]
#     while pos != 0:
#         pos = prev[pos]
#         path.append(pos)
#     return path
#
# def valid(path):
#     for i in range(len(path) - 4):
#         ds = [path[i+j] - path[i+j+1] for j in range(4)]
#         if len(set(ds)) == 1:
#             return False
#     return True
#
# dist, prev = djkstra()
# maxcost = dist[goal]
# print(dist)
# exit()
# path = get_path(goal, prev)
# grid2 = grid.copy()
# for p1, p2 in pairwise(reversed(path)):
#     grid2[p2] = {1: ">", -1: "<", 1j: "v", -1j: "^"}[p2 - p1]
# pgrid(grid2)

###########
# maxcost = 0
# cur = 0
# d = 1
# steps = 0
# while cur != goal:
#     if cur + d not in grid or steps == MAXD:
#         d = 1 if d != 1 else 1j
#         steps = 0
#     cur += d
#     maxcost += grid[cur]
#     # grid[cur] = "#"
#     steps += 1

# maxcost = 1101
maxcost = 930
# maxcost = 150
print(maxcost)
norm = lambda x: x.real / abs(x.real) if x.real != 0 else 1j * x.imag / abs(x.imag)
def viable(pos):
    dx, dy = int(goal.real - pos.real) , int(goal.imag - pos.imag)
    if pos.real > pos.imag:
        return ceil(dy / MAXD) <= ceil(dx / MIND) + 1
    else:
        return ceil(dx / MAXD) <= ceil(dy / MIND) + 1
@functools.cache
def search(cost, pos, endb):
    if pos == goal:
        return cost
    if cost > maxcost or mh_dist(pos, goal)*2 > maxcost - cost:# or not viable(pos):
        return infty
    d = norm(endb - pos)

    nxt = [pos + 4 * d*1j, pos + 4 * d*-1j]
    nxtendb = [pos + 11 * d*1j, pos + 11 * d*-1j]
    nxtcosts = [cost + sum(grid.get(pos + i * d*1j, 0) for i in range(1, 5)),
                cost + sum(grid.get(pos + i * d*-1j, 0) for i in range(1, 5))]
    if pos + d != endb:
        nxt.append(pos + d)
        nxtendb.append(endb)
        nxtcosts.append(cost + grid.get(pos + d, 0))

    out = infty
    for nc, np, nendb in zip(nxtcosts, nxt, nxtendb):
        if np not in grid:
            continue
        out = min(out, search(nc, np, nendb))
    return out

res = min(search(SCX, 4, 11), search(SCY, 4j, 11j))

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")