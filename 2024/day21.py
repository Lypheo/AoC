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

def pad2(code):
    pos_dict = numpad_pos
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
def pad(code):
    pos_dict = dirpad_pos
    pos = pos_dict["A"]
    gap = pos_dict["G"]
    out = ""
    def walk(dir):
        nonlocal out
        unit = dir/abs(dir) if dir else None
        while dir:
            out += dirs[unit]
            dir -= unit

    for num in code:
        goal = pos_dict[num]
        d = goal - pos
        if pos.real == gap.real and goal.imag == gap.imag:
            walk(d.real); walk(d-d.real)
        elif pos.imag == gap.imag and goal.real == gap.real:
            walk(d-d.real); walk(d.real)
        else:
            walk(d.real);walk(d-d.real)
        out += "A"
        pos = goal
    return out

@functools.cache
def f(chunk, depth):
    if depth == 0:
        return len(chunk)
    tf = pad(chunk)
    chunks = re.findall(r".*A", tf)
    return sum(f(c, depth-1) for c in chunks)

inp = lines(inp)
res = 0
for line in inp:
    paths = pad2(line)
    print(line, paths)
    minval = 1e99
    for path in paths:
        minval = min(minval, f(path, 2))
    res += minval * ints(line)[0]


print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")