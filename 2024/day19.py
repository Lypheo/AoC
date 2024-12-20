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

puzzle = Puzzle(year=2024, day=19)
inp = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip()
inp = puzzle.input_data

patterns, designs = blocks(inp)
patterns = patterns.split(", ")
designs = lines(designs)

@functools.cache
def f(des: str):
    if not des:
        return 1
    return sum(f(des.removeprefix(pattern)) for pattern in patterns if des.startswith(pattern))

p1 = sum(f(design) > 0 for design in designs)
p2 = sum(f(design) for design in designs)

print(f"Solution: {p1, p2}")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")