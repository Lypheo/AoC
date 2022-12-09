import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 8
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o[part]}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    trees = [[int(k) for k in n] for n in inp.splitlines()]
    ans = 0
    size = len(trees)
    for y in range(size):
        for x in range(size):
            tree = trees[y][x]
            visible = 1 if all(trees[y][xx] < tree for xx in range(x)) or \
                all(trees[y][xx] < tree for xx in range(x+1, size)) or \
                all(trees[yy][x] < tree for yy in range(y+1, size)) or \
                all(trees[yy][x] < tree for yy in range(y)) else 0
            ans += visible
    return ans

def solve_b(inp=input_data):
    trees = [[int(k) for k in n] for n in inp.splitlines()]
    ans = 0
    size = len(trees)
    def los(x, y, rx, ry):
        t = trees[y][x]
        v = 0
        for yy in ry:
            for xx in rx:
                v += 1
                if trees[yy][xx] >= t:
                    return v
        return v

    for y in range(size):
        for x in range(size):
            visible = los(x, y, range(x+1, size), range(y, y+1)) * \
                      los(x, y, range(x-1, -1, -1), range(y, y+1)) * \
                      los(x, y, range(x, x+1), range(y+1, size)) * \
                      los(x, y, range(x, x+1), range(y-1, -1, -1))
            ans = max(ans, visible)
    return ans

tests = {
    """30373
25512
65332
33549
35390""" : [21, 8]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)
#
# test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
import time
t1 = time.time_ns()
for i in range(times := 300):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")