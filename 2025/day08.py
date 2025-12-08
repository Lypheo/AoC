import os
import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from aocl import *
from functional import seq
from fn import _ as l
from pyperclip import copy

st=time.time()

puzzle = Puzzle(year=2025, day=8)
inp = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()
inp = puzzle.input_data

def eucl(p1, p2):
    return sum((p1[i]-p2[i])**2 for i in range(len(p1)))**0.5

boxes = [tuple(ints(x)) for x in lines(inp)]
pairs = sorted(combinations(boxes, 2), key=lambda x: eucl(x[0], x[1])) 

links = {box: {box} for box in boxes}
for i, (a, b) in enumerate(pairs):
    if i == 1000:
        circuits = {tuple(sorted(linked_boxes)) for linked_boxes in links.values()}
        sizes = sorted([len(v) for v in circuits])
        p1 = prod(sizes[-3:])

    if a in links[b]:
        continue
    for box in links[a].copy():
        links[box].update(links[b])
    for box in links[b].copy():
        links[box].update(links[a])
    if len(links[a]) == len(boxes):
        p2 = a[0] * b[0]
        break

print(f"Solution: {p1, p2}\n")
copy(p2)

print(f"----{(time.time()-st):.3f} s----")