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
day = 21
puzzle = Puzzle(year=2023, day=day)
inp = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""".strip()
# inp = puzzle.input_data

plots = len(inp) - inp.count("#")
D = len(lines(inp))
grid = parse_grid(lines(inp))
res = 0

# start = next(pos for pos in grid if grid[pos] == "S")
# q = {start}
# seen = {start}
# last = 0
# for i in range(50):
#     nextq = set()
#     for p in q:
#         for n in nb(p):
#             x, y = n.real, n.imag
#             if x < 0:
#                 x = D - (abs(x) % D)
#             x = x % D
#             if y < 0:
#                 y = D - (abs(y) % D)
#             y = y % D
#             ind = x + y * 1j
#             if grid[ind] != "#":
#                 nextq.add(n)
#                 seen.add(n)
#     q = nextq
#
#     print(i, len(q), len(q) - last)
#     last = len(q)

start = next(pos for pos in grid if grid[pos] == "S")
q = {start}
id_purged = set()
exp_ids = set()
odd = {}
getid = lambda p: (p.real // D, p.imag // D)

last = dd(int)
for i in range(1, 5000):
    ls = dd(set)
    for p in q:
        for n in nb(p):
            idx = getid(n)
            if idx in id_purged:
                continue
            x, y = n.real, n.imag
            if x < 0:
                x = D - (abs(x) % D)
            x = x % D
            if y < 0:
                y = D - (abs(y) % D)
            y = y % D
            ind = x + y * 1j
            if grid[ind] != "#":
                ls[idx].add(n)

    q = set().union(*ls.values())

    if not exp_ids:
        ps = {pos for pos in q if getid(pos) == (0, 0)}
        if len(ps) == 39:
            exp_ids.add((0, 0))
            odd[(0,0)] = 1 if i % 2 == 0 else 0
    else:
        for idx in exp_ids.copy():
            if idx in id_purged:
                continue
            if all(nbid in exp_ids for nbid in nb(idx)):
                q -= {pos for pos in q if getid(pos) == idx}
                id_purged.add(idx)
                print(i, idx)
                continue
            for nbid in nb(idx):
                if nbid in exp_ids:
                    continue
                # l = len([pos for pos in q if getid(pos) == nbid])
                l = len(ls[nbid])
                if l == 42 and last[nbid] == 39:
                    exp_ids.add(nbid)
                    odd[nbid] = i % 2
                last[nbid] = l

    ans = len(q)
    add = sum(42 if odd[idx] == i % 2 else 39 for idx in id_purged)
    # realadd = len([pos for pos in q if any(getid(pos) == idx for idx in id_purged)])
    # if i in [6,10, 50, 100, 500, 1000, 5000]:
    print(f"step {i}: ", end="")
    print(ans + add)

res = len(q)
print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")