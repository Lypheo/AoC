from aocd.models import Puzzle
from aocd import submit
import sys
sys.path.append("..")
from aocl import *
from functional import seq
from fn import _ as l

day = 4
puzzle = Puzzle(year=2024, day=day)
inp = puzzle.input_data

inp = lines(inp)
grid = {}
for y, line in enumerate(inp):
    for x, row in enumerate(line):
        grid[x + y*1j] = row

def count_xmas(pos):
    return sum("".join([grid.get(pos + v*i, "") for i in range(4)]) == "XMAS" for v in nbd(0))

res = seq(grid.keys()).map(count_xmas).sum()
print(f"Solution 1: {res}\n")

def count_mas(pos):
    return sum("".join([grid.get(pos + v*i, "") for i in sri(-1, 1)]) == "MAS" for v in nbd(0) if abs(v) > 1)

res = seq(grid.keys()).map(count_mas).count(l == 2)
print(f"Solution 2: {res}\n")