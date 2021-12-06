import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 6
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    for i,o in tests.items():
        if (ao := solution(i)) != o[part]:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    fish = [int(x) for x in inp.split(",")]
    for i in range(80):
        newf = []
        for f in fish:
            if f > 0:
                newf.append(f-1)
            else:
                newf.append(6)
                newf.append(8)
        fish = newf
    return len(fish)

def solve_b(inp=input_data):
    fish = [int(x) for x in inp.split(",")]
    fish = [fish.count(k) for k in range(9)]
    for _ in range(256):
        newf = [0]*9
        for i in range(1,9):
            newf[i-1] = fish[i]
        newf[8] = fish[0]
        newf[6] += fish[0]
        fish = newf
    return sum(fish)

tests = {"""3,4,3,1,2""": [5934, 26984457539]
}

# test(tests, solve_a, 0)
a = solve_a()
print(f"Part 1: {a}\n")
# submit(a, part="a", day=day, year=2021)

# test(tests, solve_b, 1)
b = solve_b()
if b:
    print(f"Part 2: {b}")
#     submit(b, part="b", day=day, year=2021)
