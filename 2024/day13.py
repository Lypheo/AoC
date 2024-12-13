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

day = 13
puzzle = Puzzle(year=2024, day=day)
inp = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()
inp = puzzle.input_data

machines = blocks(inp)
res = 0


for mach in machines:
    a, b, p = lines(mach)
    A, B, Prize = [complex(*ints(line)) for line in [a, b, p]]
    Prize += + 10000000000000 + 10000000000000j

    # a * A.x + b * B.x = Prize.x
    # a * A.y + b * B.y = Prize.y
    # b = (Prize.x - a * A.x) / B.x
    # a * A.y + (Prize.x - a * A.x) / B.x * B.y = Prize.y
    # a * A.y + Prize.x * B.y/B.x - a * A.x * B.y/B.x  = Prize.y
    # a * A.y - a * A.x * B.y/B.x  = Prize.y - Prize.x * B.y/B.x
    # a  = (Prize.y - Prize.x * B.y/B.x) / (A.y - A.x * B.y/B.x)

    a = (Prize.imag - Prize.real * B.imag/B.real) / (A.imag - A.real * B.imag/B.real)
    b = (Prize.real - a * A.real) / B.real
    if abs(a - round(a)) > 0.01 or abs(b - round(b)) > 0.01:
        continue
    res += round(a)*3 + round(b)

print(f"Solution: {res}\n")
copy(res)
# submit(res)

print("----%.2f s----"%(time.time()-st))
