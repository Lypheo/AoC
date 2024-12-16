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

day =
puzzle = Puzzle(year=2024, day=day)
inp = """

""".strip()
inp = puzzle.input_data

inp = lines(inp)
res = 0


print(f"Solution: {res}\n")
copy(res)
# submit(res)

print("----%.2f s----"%(time.time()-st))
