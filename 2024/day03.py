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

day = 3
puzzle = Puzzle(year=2024, day=day)
inp = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

""".strip()
inp = puzzle.input_data

def f(chunk):
    return sum(prod(ints(mul)) for mul in re.findall(r"mul\(\d+,\d+\)", chunk))

res = 0
a = inp
while True:
    s = re.split(r"don't\(\)", a, maxsplit=1)
    res += f(s[0])
    if not(len(s) > 1 and "do()" in s[1]):
        break
    a = re.split(r"do\(\)", s[1], maxsplit=1)[1]

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")