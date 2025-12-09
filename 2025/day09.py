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

puzzle = Puzzle(year=2025, day=9)
inp = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()
inp = puzzle.input_data

points = [complex(*ints(line)) for line in lines(inp)]
res = 0

def area(a, b):
    return int(abs(a.real - b.real) + 1) * int(abs(a.imag - b.imag) + 1)
def sign(x):
    return -1 if x < 0 else 1
def norm(c):
    return c/abs(c.real + c.imag)

def angle(v1, v2):
    assert not (v1.real == v2.real == 0 or v1.imag == v2.imag == 0)
    return -1 if v1 * 1j == v2 else 1

edges = seq(points + [points[0]]).sliding(2).map(tuple).to_list()
orths = {} # orthonormal pointing outside
total_angle = 0
for edge1, edge2 in seq(edges + [edges[0]]).sliding(2):
    dir1 = norm(edge1[1] - edge1[0])
    dir2 = norm(edge2[1] - edge2[0])
    total_angle += angle(dir1, dir2)
    orths[edge1] = dir1 * 1j
orths = {k: v*sign(total_angle) for k,v in orths.items()}

invalid_dirs_from_point = dd(list)
for edge1, edge2 in seq(edges + [edges[0]]).sliding(2):
    dir1 = norm(edge1[1] - edge1[0])
    dir2 = norm(edge2[1] - edge2[0])
    if orths[edge1] != dir2:
        invalid_dirs_from_point[edge1[1]].extend([orths[edge1], dir1])

def valid(a,b,c,d):
    if any(a.real < p.real < c.real and a.imag < p.imag < c.imag for p in points):
        return False
    for e1, e2 in edges:
        dir = norm(e2 - e1)
        if dir.real:
            s, e = min(e1.real, e2.real), max(e1.real, e2.real)
            if s <= a.real and e >= b.real and a.imag < e1.imag < c.imag:
                return False
        else:
            s, e = min(e1.imag, e2.imag), max(e1.imag, e2.imag)
            if s <= a.imag and e >= c.imag and a.real < e1.real < b.real:
                return False
    corner_dirs = {a: [1j, 1], b: [1j, -1], c: [-1j, -1], d: [-1j, 1]}
    if any(invalid_dir in dirs for corner, dirs in corner_dirs.items() for invalid_dir in invalid_dirs_from_point[corner]):
        return False
    return True

for p1,p2 in combinations(points, 2):
    a = complex(min(p1.real, p2.real), min(p1.imag, p2.imag))
    b = complex(max(p1.real, p2.real), min(p1.imag, p2.imag))
    c = complex(max(p1.real, p2.real), max(p1.imag, p2.imag))
    d = complex(min(p1.real, p2.real), max(p1.imag, p2.imag))
    if valid(a,b,c,d):
        res = max(res, area(p1, p2))
    

print(f"Solution: {res}\n")
copy(res)

print(f"----{(time.time()-st):.3f} s----")