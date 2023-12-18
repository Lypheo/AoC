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
t1 = time.time_ns()

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

maxcost = 0
cur = 0
d = 1
steps = 0
while cur != goal:
    if cur + d not in grid or steps == MAXD:
        d = 1 if d != 1 else 1j
        steps = 0
    cur += d
    maxcost += grid[cur]
    steps += 1

norm = lambda x: x.real / abs(x.real) if x.real != 0 else 1j * x.imag / abs(x.imag)

print(maxcost)
mincost = maxcost
seen = {(4, 10): SCX, (4j, 10j): SCY}
for i in range(1000):
    print(i, mincost, len(seen))
    nxt = []
    newseen = {}
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
                r = (pos + d2*4, pos + d2 * 10)
                if dcost < mincost and mh_dist(r[0], goal) <= mincost - dcost:
                    newseen[r] = min(dcost, newseen.get(r, infty))
            cost += grid.get(pos + d, 0)
    seen = newseen

print(f"Solution: {mincost}\n")
# submit(res)

# import time
t2 = time.time_ns()
print(f"Time: {(t2-t1) / 1000000} ms")