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

puzzle = Puzzle(year=2024, day=21)
inp = """
029A
980A
179A
456A
379A
""".strip()
inp = puzzle.input_data

numpad_pos = {'7': 0, '8': 1, '9': 2, '4': 1j, '5': (1+1j), '6': (2+1j), '1': 2j, '2': (1+2j), '3': (2+2j), '0': (1+3j), 'A': (2+3j), 'G': 3j}
dirpad_pos = {'^': 1, 'A': 2, '<': 1j, 'v': (1+1j), '>': (2+1j), 'G': 0}
dirs = {1j: "v", -1j: "^", 1: ">", -1:"<"}

def expand(code, numpad=True):
    pos_dict = numpad_pos if numpad else dirpad_pos
    pos = pos_dict["A"]
    gap = pos_dict["G"]
    outs = [""]
    def app(x, a=outs):
        a[:] = [o + x for o in a]

    def walk(dir):
        out = ""
        unit = dir/abs(dir) if dir else None
        while dir:
            out += dirs[unit]
            dir -= unit
        return out

    for num in code:
        goal = pos_dict[num]
        d = goal - pos
        if pos.real == gap.real and goal.imag == gap.imag:
            app(walk(d.real)); app(walk(d-d.real))
        elif pos.imag == gap.imag and goal.real == gap.real:
            app(walk(d-d.real)); app(walk(d.real))
        else:
            oouts = outs.copy()
            app(walk(d-d.real)); app(walk(d.real))
            app(walk(d.real), oouts); app(walk(d-d.real), oouts)
            outs += oouts
        app("A")
        pos = goal
    return outs

@functools.cache
def f(chunk, depth, part2=False):
    if depth == 0:
        return len(chunk)
    ways = expand(chunk, numpad = depth==(26 if part2 else 3))
    return min(sum(f(c, depth-1, part2) for c in re.findall(r".*?A", way)) for way in ways)

inp = lines(inp)
p1, p2 = 0, 0
for line in inp:
    p1 += f(line, 3, False) * ints(line)[0]
    p2 += f(line, 26, True) * ints(line)[0]

print(f"Solution: {p1, p2}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")