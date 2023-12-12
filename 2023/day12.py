import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from itertools import permutations
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
from aocl import *
day = 12
puzzle = Puzzle(year=2023, day=day)
inp = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip()
inp = puzzle.input_data


inp = lines(inp)
res = 0
# mult = 1
# for line in inp:
#     conds, groups = line.split(" ")
#     groups = list(map(int, groups.split(",")))*mult
#     conds = "?".join([conds]*mult)
#     # print(conds, groups)
#     # continue
#     unk = [i for i, x in enumerate(conds) if x == "?"]
#     arrs = 0
#     for p in product([".", "#"], repeat=len(unk)):
#         # print(p, conds)
#         newconds = conds
#         for spring in p:
#             newconds = newconds.replace("?", spring, 1)
#         spring_gs = re.findall(r"#+", newconds)
#         # print(newconds, len(spring_gs) == len(groups))
#         if len(spring_gs) == len(groups) and all(len(spring_gs[i]) == groups[i] for i in range(len(groups))):
#             arrs += 1
#     print(conds, groups, arrs)
#     res += arrs
# print(res)
# exit()
def dbg(func):
    def wrapper(*args, **kwargs):
        v = func(*args, **kwargs)
        print(args, " | Out: ", v)
        return v
    return wrapper

# @dbg
@functools.cache
def f(s, counts, hash_allowed=True):
    s = s.strip(".")
    if not s or not counts:
        return (s and not "#" in s) or (not s and not counts)

    c = counts[0]
    stripped = s.lstrip("#")
    hl = len(s) - len(stripped)
    if hl == 0:
        return (f("#" + stripped[1:], counts) if hash_allowed else 0) + f("." + stripped[1:], counts)
    elif hl == c:
        return f(stripped, counts[1:], stripped and stripped[0] == ".")
    elif hl > c:
        return 0
    elif hl < c:
        return f("#" + stripped[1:], (c - hl, *counts[1:])) if stripped and stripped[0] == "?" else 0

mult = 5
for line in inp:
    conds, groups = line.split(" ")
    groups = list(map(int, groups.split(",")))*mult
    conds = "?".join([conds]*mult)
    res += f(conds, tuple(groups))

print(f"Solution: {res}\n")
# submit(res)

import time
t1 = time.time_ns()
for i in range(times := 50):
    for line in inp:
        conds, groups = line.split(" ")
        groups = list(map(int, groups.split(","))) * mult
        conds = "?".join([conds] * mult)
        res += f(conds, tuple(groups))
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")