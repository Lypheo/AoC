import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 3
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    inp = inp.splitlines()
    summ = 0
    for l in inp:
        ln = int(len(l)/2)
        first = l[:ln]
        second = l[ln:]
        both = set(first).intersection(set(second))
        b = both.pop()
        summ += (ord(b) - ord("A") + 27) if b.isupper() else (ord(b) - ord("a") + 1)
    return summ

def solve_b(inp=input_data):
    inp = inp.splitlines()
    summ = 0
    for i in range(int(len(inp)/3)):
        rucks = inp[i*3:i*3+3]
        badge = set(rucks[0]).intersection(set(rucks[1])).intersection(set(rucks[2]))
        b = badge.pop()
        summ += (ord(b) - ord("A") + 27) if b.isupper() else (ord(b) - ord("a") + 1)
    return summ

tests = {
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

# test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")