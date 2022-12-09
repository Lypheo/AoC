import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 9
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
    inp = [(line.split(" ")[0], int(line.split(" ")[1])) for line in inp.splitlines()]
    posh, post = 0, 0
    hist = set()
    hist.add(post)
    for move, length in inp:
        for step in range(length):
            posh += {"U": 1j, "D": -1j, "L":-1, "R":1}[move]
            if abs(posh.real - post.real) > 1 or abs(posh.imag - post.imag) > 1:
                if posh.real == post.real:
                    post += 1j if posh.imag > post.imag else -1j
                elif posh.imag == post.imag:
                    post += 1 if posh.real > post.real else -1
                else:
                    post += 1j if posh.imag > post.imag else -1j
                    post += 1 if posh.real > post.real else -1
            print(posh, post)
            hist.add(post)

    return len(hist)

def solve_b(inp=input_data):
    inp = [(line.split(" ")[0], int(line.split(" ")[1])) for line in inp.splitlines()]
    pos = [0]*10
    hist = set()
    hist.add(pos[-1])
    for move, length in inp:
        for step in range(length):
            pos[0] += {"U": 1j, "D": -1j, "L":-1, "R":1}[move]
            for i in range(1,10):
                posh = pos[i-1]
                post = pos[i]
                if abs(posh.real - post.real) > 1 or abs(posh.imag - post.imag) > 1:
                    if posh.real == post.real:
                        post += 1j if posh.imag > post.imag else -1j
                    elif posh.imag == post.imag:
                        post += 1 if posh.real > post.real else -1
                    else:
                        post += 1j if posh.imag > post.imag else -1j
                        post += 1 if posh.real > post.real else -1
                pos[i] = post
            hist.add(pos[-1])

    return len(hist)

tests = {
    """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""" : [13, 1]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

# test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")