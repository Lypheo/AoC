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
from functional import seq
from fn import _ as l
from pyperclip import copy

st=time.time()

day = 12
puzzle = Puzzle(year=2024, day=day)
inp = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""".strip()
inp = puzzle.input_data

grid = parse_grid(inp)
res = 0
seen = set()
regions = []

for p in grid:
    if p in seen:
        continue
    seen.add(p)
    region = {p}
    q = [p]
    while q:
        x = q.pop()
        for pp in nb(x):
            if grid.get(pp) == grid[p] and pp not in seen:
                seen.add(pp)
                q.append(pp)
                region.add(pp)
        # print(p, q)
    regions.append(region)

def cost(region):
    area = len(region)
    perimeter = 0
    for p in region:
        for pp in nb(p):
            if pp not in region:
                perimeter += 1
    return area * perimeter

def cost2(region):
    area = len(region)
    nregion = seq(region).map(l*2).map(lambda x: [x, x+1, x+1j, x+1+1j]).flatten().to_set()
    corners = 0
    for p in nregion:
        nbs = {x for x in nb(p) if x in nregion}
        diags = {x for x in nbd(p) if x in nregion} - nbs
        if len(nbs) == 2 and len(diags) in [1,2] or len(nbs) == 4 and len(diags) == 3:
            corners += 1
    num_sides = corners
    # perimeter = set()
    # for p in region:
    #     for pp in nb(p):
    #         if pp not in region:
    #             perimeter.add(pp)
    #
    # sides_seen = set()
    # sides = []
    # for p in perimeter:
    #     if p in sides_seen:
    #         continue
    #     sides_seen.add(p)
    #     b = False
    #     for dir in [1, 1j]:
    #         side = {p}
    #         for sign in [1, -1]:
    #             pp = p
    #             dir *= sign
    #             while pp + dir in perimeter:
    #                 pp += dir
    #                 side.add(pp)
    #                 sides_seen.add(pp)
    #         if len(side) > 1:
    #             sides.append(side)
    #             b = True
    #     if not b:
    #         sides.append({p})
    #
    # num_sides = len(sides)
    # for side in sides:
    #     if bar := seq(side).map(lambda x: seq(nb(x)).filter(lambda y: y in region).len()).find(l >= 3):
    #         num_sides +=  bar - 1
    #         continue
    #     if len(side) > 1:
    #         continue
    #     p = side.pop()
    #     foo = seq(perimeter).filter(lambda x: x in nbd(p)).map(p - l).to_set()
    #     if len(foo) == 2 and foo.pop() == - foo.pop():
    #         num_sides += 1
    print(grid.get(region.pop()), area, num_sides)
    return area * num_sides

res = sum(cost2(region) for region in regions)
print(f"Solution: {res}\n")
copy(res)
# submit(res)

print("----%.2f s----"%(time.time()-st))
