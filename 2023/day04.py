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
day = 4
puzzle = Puzzle(year=2023, day=day)
inp = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()
# inp = puzzle.input_data

#p1
# inp = lines(inp)
# res = 0
# idx = 0
# for l in inp:
#     idx += 1
#     l = l.split(": ")[1]
#     winning, mine = l.split(" | ")
#     print(winning)
#     winning, mine = ints(winning), ints(mine)
#     overlap = set(winning) & set(mine)
#     if overlap:
#         res += 2 ** (len(overlap) - 1)

#p2
inp = lines(inp)
res = 0
copies = dd(lambda: 1)
for idx, l in enumerate(inp, 1):
    copies[idx]
    l = l.split(": ")[1]
    winning, mine = l.split(" | ")
    winning, mine = ints(winning), ints(mine)
    overlap = set(winning) & set(mine)
    if overlap:
        for i in range(idx+1,idx+1+len(overlap)):
            copies[i] += copies[idx]
print(copies)
res = sum(copies.values())
print(f"Solution: {res}\n")
# submit(out)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")