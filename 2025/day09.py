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
# inp = puzzle.input_data

points = [complex(*ints(line)) for line in lines(inp)]
res = 0
def area(a, b):
    return int(abs(a.real - b.real) + 1) * int(abs(a.imag - b.imag) + 1)
def sign(x):
    return -1 if x < 0 else 1

def angle(v1, v2):
    assert not (v1.real == v2.real == 0 or v1.imag == v2.imag == 0)
    if v1.real:
        return 1 if sign(v1.real) == sign(v2.imag) else -1
    else:
        return 1 if sign(v1.imag) != sign(v2.real) else -1

edges = seq(points + [points[0]]).sliding(2).map(tuple).to_list()
orths = {} # orthonormal pointing outside
total_angle = 0
for edge1, edge2 in seq(edges + [edges[0]]).sliding(2):
    dir1 = edge1[1] - edge1[0]    
    dir2 = edge2[1] - edge2[0]
    total_angle += angle(dir1, dir2)
    orths[edge1] = -dir2/abs(dir2.real + dir2.imag)
    print(edge1, edge2, dir1, dir2, angle(dir1, dir2))
orths = {k: v*sign(total_angle) for k,v in orths.items()}
print(points)
print(edges)
print(orths)
print(total_angle)

def isSubedge(rect_edge, edge):
    rect_dir, dir = rect_edge[1] - rect_edge[0], edge[1] - edge[0]
    if rect_dir.imag * dir.imag + rect_dir.real * dir.real == 0:
        return False
    if dir.real:
        return all(min(p.real for p in rect_edge) <= ep.real <= max(p.real for p in rect_edge) for ep in edge)
    else:
        return all(min(p.imag for p in rect_edge) <= ep.imag <= max(p.imag for p in rect_edge) for ep in edge)

def valid(a,b,c,d):
    if any(a.real < p.real < c.real and c.imag < p.imag < a.imag for p in points):
        return False
    rect_orths = {(a,b): 1j, (b,c): 1, (c,d): -1j, (d,a):-1}
    for edge in edges:
        for rect_edge, rect_orth in rect_orths.items():
            if isSubedge(rect_edge, edge):
                edge_orth = orths[edge]
                assert edge_orth in rect_orths.values()
                if edge_orth != rect_orth:
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