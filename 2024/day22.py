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

puzzle = Puzzle(year=2024, day=22)
inp = """
1
2
3
2024
""".strip()
inp = puzzle.input_data

bdic = dd(dict)
def getSecret(num,n):
    id_ = num
    hist = []
    last = num % 10
    for _ in range(n):
        num = ((num*64) ^ num) % 16777216
        num = (int(num/32) ^ num) % 16777216
        num = ((num*2048) ^ num) % 16777216
        mod10 = (num % 10)
        hist.append((mod10, mod10 - last))
        if len(hist) >= 4:
            sq = tuple(x[1] for x in hist[-4:])
            if id_ not in bdic[sq]:
                bdic[sq][id_] = mod10
        last = mod10
    return num

inp = lines(inp)
p1 = 0
for line in inp:
    p1 += getSecret(ints(line)[0], 2000)

p2 = 0
for four in product(sri(-9,9), repeat=4):
    bananas = sum(bdic[four].values())
    if bananas > p2:
        p2 = bananas
print(f"Solution: {p1, p2}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")