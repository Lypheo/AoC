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
day = 13
puzzle = Puzzle(year=2023, day=day)
inp = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

##.#.##...####.
#####..#...##..
##.##.#.#####.#
.##.#..##..##..
###..#.#####.#.
###..#.#####.#.
.##.#..##..##..
##.##.#.#####.#
#####..#...##..
##.#.##..#####.
...#...#....###
##.#.###.###..#
..#.###.#.#....
####...#.#.#...
.#..#....##.#.#
....####.###.##
....####.###.##
""".strip()

inp = puzzle.input_data


# B = inp.split("\n\n")
# res = 0
# As = []
# lenx, leny = 0, 0
# for b in B:
#     rows = b.split("\n")
#     leny, lenx = len(rows), len(rows[0])
#     A = [row for row in rows]
#     As.append(A)
#
# def find_axis(A):
#     leny, lenx = len(A), len(A[0])
#     for y in range(1, leny):
#         s = max(0, y - (leny-y))
#         e = min(leny, y + y)
#         if "".join(A[s:y]) == "".join(reversed(A[y:e])):
#             return y
#     return 0
#
# for A in As:
#     leny, lenx = len(A), len(A[0])
#     res += find_axis(A) * 100
#     A = ["".join(A[y][x] for y in range(leny)) for x in range(lenx)]
#     res += find_axis(A)

B = inp.split("\n\n")
res = 0
As = []
lenx, leny = 0, 0
for b in B:
    rows = b.split("\n")
    leny, lenx = len(rows), len(rows[0])
    A = [row for row in rows]
    As.append(A)

def diff(s1, s2):
    return sum(x1 != x2 for x1, x2 in zip(s1, s2))
def find_axis(A):
    leny, lenx = len(A), len(A[0])
    for y in range(1, leny):
        s = max(0, y - (leny-y))
        e = min(leny, y + y)
        if diff("".join(A[s:y]), "".join(reversed(A[y:e]))) == 1:
            return y
    return 0

for A in As:
    leny, lenx = len(A), len(A[0])
    res += find_axis(A) * 100
    A = ["".join(A[y][x] for y in range(leny)) for x in range(lenx)]
    res += find_axis(A)

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")