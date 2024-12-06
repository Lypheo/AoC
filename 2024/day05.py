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

day = 5
puzzle = Puzzle(year=2024, day=day)
inp = puzzle.input_data

rules, updates = blocks(inp)
rules = [ints(line) for line in lines(rules)]
reqs = dd(list)
for a,b in rules:
    reqs[b].append(a)
updates = [seq(ints(line)) for line in lines(updates)]

p1, p2 = 0, 0
for update in updates:
    valid = update.enumerate().smap(lambda i, a: update[i+1:].intersection(reqs[a]).empty()).all()
    p1 += update[update.len()//2] if valid else 0
    if not valid:
        for i in range(update.len()//2 + 1):
            mid = update.find(lambda x: not any(b in reqs[x] for b in update))
            update = update.filter(l != mid)
        p2 += mid

print(f"Solution: {p1}, {p2}\n")
# submit(res)