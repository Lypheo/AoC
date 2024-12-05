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
inp = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()
inp = puzzle.input_data

rules, updates = blocks(inp)
res = 0
rules = [ints(line) for line in lines(rules)]
reqs = dd(list)
for a,b in rules:
    reqs[b].append(a)
updates = [ints(line) for line in lines(updates)]

for update in updates:
    valid = True
    for ax, a in enumerate(update):
        if any(b in reqs[a] for b in update[ax+1:]):
            valid = False
            break
    if not valid:
        new = []
        while len(new) < len(update):
            for a in update:
                if a not in new and not any(b in reqs[a] for b in set(update)-set(new)):
                    new.append(a)

        res += new[len(new)//2]

print(f"Solution: {res}\n")
# submit(res)
