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
    return area * corners

p1 = sum(cost(region) for region in regions)
p2 = sum(cost2(region) for region in regions)
print(f"Solution: {p1, p2}\n")
copy(res)

print("----%.2f s----"%(time.time()-st))
