import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 4
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) != o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

from collections import defaultdict as dd
def solve_a(inp=input_data):
    inp = inp.split("\n\n")
    num = [int(x) for x in inp[0].split(",")]
    bs = [[[int(y) for y in x.split()] for x in k.split("\n")] for k in inp[1:]]
    scans = [[(x, y) for y in range(5)]  for x in range (5)]
    scans += [[(x, y) for x in range(5)]  for y in range (5)]
    for i in range(1, len(num)):
        a = num[:i]
        marked = dd(list)
        for bi, b in enumerate(bs):
            for yi, y in enumerate(b):
                for xi, x in enumerate(y):
                    if x in a:
                        marked[bi].append((yi, xi))

        for bi,m in marked.items():
            for s in scans:
                if all(e in m for e in s):
                    return (sum(sum(row) for row in bs[bi]) - sum(bs[bi][y][x] for y,x in m)) * a[-1]

def solve_b(inp=input_data):
    inp = inp.split("\n\n")
    num = [int(x) for x in inp[0].split(",")]
    Bs = inp[1:]
    bs = [[[int(y) for y in x.split()] for x in k.split("\n")] for k in Bs]
    scans = [[(x, y) for y in range(5)]  for x in range (5)]
    scans += [[(x, y) for x in range(5)]  for y in range (5)]
    scores = dd(list)
    for i in range(1, len(num)):
        a = num[:i]
        marked = dd(list)
        for bi, b in enumerate(bs):
            for yi, y in enumerate(b):
                for xi, x in enumerate(y):
                    if x in a:
                        marked[bi].append((yi, xi))

        for bi,m in marked.items():
            for s in scans:
                if all(e in m for e in s):
                    score = (sum(sum(row) for row in bs[bi]) - sum(bs[bi][y][x] for y,x in m)) * a[-1]
                    scores[bi] = score
                    if len(scores) == len(bs):
                        return score


tests_a = {
    """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""" : 4512
}

a = solve_a()
print(f"Part 1: {a}\n")
# test(tests_a, solve_a)
# submit(a, part="a", day=day, year=2021)

tests_b = {
    """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7""" : 1924
}

# test(tests_b, solve_b)
b = solve_b()
if b:
    print(f"Part 2: {b}")
    # submit(b, part="b", day=day, year=2021)


import time
t1 = time.time_ns()
for i in range(times := 10):
    solve_a()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(times)} ns")