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
# SCX, SCY = 4, 36
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

maxcost = 1101
# maxcost = infty
print(maxcost)
norm = lambda x: x.real / abs(x.real) if x.real != 0 else 1j * x.imag / abs(x.imag)
def viable(pos):
    dx, dy = int(goal.real - pos.real) , int(goal.imag - pos.imag)
    if pos.real > pos.imag:
        return ceil(dy / MAXD) <= ceil(dx / MIND) + 1
    else:
        return ceil(dx / MAXD) <= ceil(dy / MIND) + 1

mem = dd(list)
# @functools.cache
def search(cost, pos, endb):
    d = norm(endb - pos)
    if pos in mem:
        for e, v in mem[pos]:
            if norm(e - pos) == d and abs(e - pos) >= abs(pos - endb):
                return v
    if pos == goal:
        return cost
    if cost > maxcost or mh_dist(pos, goal)*2 > maxcost - cost:# or not viable(pos):
        mem[pos].append((endb, infty))
        return infty

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
    mem[pos].append((endb, out))
    return out

# res = min(search(SCX, 4, 11), search(SCY, 4j, 11j))

# mincost = maxcost
mincost = 1500
# mincost = infty
# states = [(SCX, 4, 10), (SCY, 4j, 10j)]
seen = {(4, 10): SCX, (4j, 10j): SCY}
for i in range(1000):
    # states = sorted(states, key=lambda state: mh_dist(state[1], goal))[:100000]
    # states = [state for state in states if state[0] <= mincost and mh_dist(state[1], goal)*3 <= mincost - state[0]]
    print(i, mincost, len(seen))
    nxt = []
    for (start, end), cost in seen.items():
        d = norm(end - start)
        for pos in ip(start, end):
            if pos not in grid:
                break
            if pos == goal:
                mincost = min(mincost, cost)
                break
            for d2 in (d*1j, d*-1j):
                if pos + d2*4 not in grid:
                    continue
                dcost = cost + sum(grid[p] for p in ip(pos + d2, pos + d2 * 4))
                nxt.append((dcost, pos + d2*4, pos + d2 * 10))
            cost += grid.get(pos + d, 0)
    # states = nxt
    for cost, s, e in nxt:
        r = (s, e)
        seen[r] = min(seen.get(r, infty), cost)
    seen = {k: v for k,v in seen.items() if v <= mincost}


# print(f"Solution: {mincost}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")