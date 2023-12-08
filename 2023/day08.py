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
day = 8
puzzle = Puzzle(year=2023, day=day)
inp = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()
inp = puzzle.input_data


inp = lines(inp)
res = 0

inst, graph = inp[0], inp[2:]
g = {}
for line in graph:
    p, c = line.split(" = ")
    c = c.split(", ")
    c = [x.strip("()") for x in c]
    g[p] = tuple(c)

cur = [x for x in g.keys() if x.endswith("A")]
res = 0
def find_steps(start):
    node = start
    steps = 0
    for run in repeat(inst):
        for ins in run:
            if node.endswith("Z"):
                return steps
            else:
                steps += 1

            dr = 0 if ins == "L" else 1
            node = g[node][dr]

from math import lcm
stepl = [find_steps(x) for x in cur]
from math import gcd
lcm = 1
for i in stepl:
    lcm = lcm*i//gcd(lcm, i)
res = lcm
print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")