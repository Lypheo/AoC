from datetime import datetime
import time
import functools, itertools, collections, re, math
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data
# print(input_data)

def solve_a(inp=input_data):
    masses = [int(i) for i in inp.split("\n")]
    total = 0
    for i in masses:
        total += math.floor(i/3) -2
    return total

def solve_b(inp=input_data):
    masses = [int(i) for i in inp.split("\n")]
    total = 0
    for i in masses:
        fuel = (i//3) - 2
        diff = fuel
        while True:
            diff = ((diff)//3) - 2
            if diff > 0:
                fuel += diff
            else: 
                break
                
        total += fuel

    return total

a = solve_a()
print(f"Part 1: {a}")
# submit(a, part="a", day=day, year=2019)

b = solve_b()
if b: print(f"Part 2: {b}")
# submit(b, part="b", day=day, year=2019)
