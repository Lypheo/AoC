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

puzzle = Puzzle(year=2024, day=23)
inp = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip()
inp = puzzle.input_data
#
inp = lines(inp)
res = 0
edges = dd(list)
for line in inp:
    a, b = line.split("-")
    edges[a].append(b)
    edges[b].append(a)

cliques = set(tuple(sorted([a,b])) for a in edges for b in edges[a])
while True:
    if len(list(cliques)[0]) == 3:
        p1 = sum(any(n.startswith("t") for n in c) for c in cliques)
    nxt = set()
    for clique in cliques:
        for n in set.intersection(*[set(edges[x]) for x in clique]) - set(clique):
            nxt.add(tuple(sorted([n, *clique])))
    if not nxt:
        p2 =  ",".join(sorted(cliques.pop()))
        break
    cliques = nxt

print(f"Solution: {p1, p2}\n")
print(f"----{(time.time()-st):.3f} s----")