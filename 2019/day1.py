from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
	return None

def solve_b(inp=input_data):
	return None

a = solve_a()
print("Part 1: {a}")
# submit(a, part="a", day=day, year=2019)

b = solve_b()
if b: print("Part 2: {b}")
# submit(b, part="b", day=day, year=2019)
