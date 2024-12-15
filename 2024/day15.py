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

day = 15
puzzle = Puzzle(year=2024, day=day)
inp = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip()
inp = puzzle.input_data

inp = blocks(inp)
# inp[0] = inp[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
grid = parse_grid(inp[0])
moves = inp[1].replace("\n", "")
res = 0
mmap = {"^": -1j, "v": 1j, ">": 1, "<": -1}
pos = grid.keys().seq().find(lambda k: grid[k] == "@")

def move_p(p, d):
    if grid.get(p + d) == "#":
        return False
    elif grid.get(p + d) == ".":
        grid[p + d], grid[p] = grid[p], grid[p + d]
        return True
    else:
        if move_p(p + d, d):
            grid[p + d], grid[p] = grid[p], grid[p + d]
            return True
        return False

for move in moves:
    dir = mmap[move]
    if move_p(pos, dir):
        pos += dir


pgrid(grid)
# res = grid.items().seq().filter(lambda x: x[1] == "O").sum(lambda x: x[0].real + x[0].imag * 100)
for p, v in grid.items():
    if v == "O":
        print(p.real + p.imag * 100)
        res += p.real + p.imag * 100
print(f"Solution: {res}\n")
copy(res)
# submit(res)

print("----%.2f s----"%(time.time()-st))
