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

day = 1
puzzle = Puzzle(year=2024, day=day)
inp = """
""".strip()
inp = puzzle.input_data

inp = lines(inp)

a = seq(inp).map(ints).map(l[0]).sorted()
b = seq(inp).map(ints).map(l[1]).sorted()
p1 = a.zip(b).smap(l - l).map(abs).sum()
p2 = a.sum(lambda x: x * b.to_list().count(x))
print(f"Solution: {p1}, {p2}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")²