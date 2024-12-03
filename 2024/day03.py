from aocd.models import Puzzle
from math import prod
import sys, re
sys.path.append("..")
from aocl import *
from functional import seq

puzzle = Puzzle(year=2024, day=3)
inp = puzzle.input_data
def f(chunk):
    return seq(re.findall(r"mul\(\d+,\d+\)", chunk)).map(ints).map(prod).sum()

res = seq(re.split(r"do\(\)", inp)).map(lambda x: re.split(r"don't\(\)", x)[0]).map(f).sum()
print(f"Solution: {res}\n")