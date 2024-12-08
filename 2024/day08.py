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
st=time.time()

day = 8
puzzle = Puzzle(year=2024, day=day)
inp = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()
inp = puzzle.input_data

grid = parse_grid(inp)

part1, part2 = set(), set()
for p1,v1 in grid.items():
    for p2,v2 in grid.items():
        if v1 == "." or v1 != v2 or p1 == p2:
            continue
        d = p2 - p1
        part1.update({p1 - d, p2 + d})
        part2.update(seq.range(len(grid)).take_while(lambda i: (p1 - i*d) in grid).map(p1 - l*d))
        part2.update(seq.range(len(grid)).take_while(lambda i: (p2 + i*d) in grid).map(p2 + l*d))

part1 = part1.intersection(grid.keys())
part2 = part2.intersection(grid.keys())

ans1, ans2 = len(part1), len(part2)
print(f"Solution: {ans1}, {ans2}\n")
# submit(res)

print("----%.2f s----"%(time.time()-st))
