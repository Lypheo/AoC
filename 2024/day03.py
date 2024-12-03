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
inp = puzzle.input_data

def f(chunk):
    return seq(re.findall(r"mul\(\d+,\d+\)", chunk)).map(ints).map(prod).sum()

res = seq(re.split(r"do\(\)", inp)).map(lambda x: re.split(r"don't\(\)", x)[0]).map(f).sum()

print(f"Solution: {res}\n")
