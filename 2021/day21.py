import time
import functools, itertools, collections, re
from pprint import pprint

import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 21
puzzle = Puzzle(year=2021, day=day)
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
    s = [0,0]
    pos = [int(n[-1]) for n in inp.splitlines()]
    dice = 1
    k = 0
    for i in itertools.count(0):
        v = 0
        for _ in range(dice, dice+3):
            v += dice
            k += 1
            if dice < 100:
                dice += 1
            else:
                dice = 1

        for _ in range(v):
            pos[i % 2] += 1
            if pos[i % 2] == 11:
                pos[i % 2] = 1
        s[i % 2] += pos[i % 2]
        print(s, i)
        if (s[i % 2]) >= 1000:
            return s[(i+1) % 2]* k

    return

def solve_b(inp=input_data):
    spos = [int(n[-1]) for n in inp.splitlines()]

    def wrap10(v, inc):
        v += inc
        if v >= 11:
            v = v % 10
        return v

    vadd = lambda a,b: [ac + bc for ac,bc in zip(a,b)]
    from functools import cache
    @cache
    def wins(score1, score2, p1, p2, turn):
        pso = [p1, p2]
        scoreso = [score1, score2]
        wn = [0,0]
        for roll in itertools.product(range(1,4), range(1,4), range(1,4)):
            ps = pso.copy()
            scores = scoreso.copy()
            ps[turn] = wrap10(ps[turn], sum(roll))
            scores[turn] += ps[turn]
            if scores[turn] >= 21:
                wn[turn] += 1
            else:
                wn = vadd(wn, wins(*scores, *ps, 1 if turn == 0 else 0))

        return tuple(wn)

    return max(wins(0, 0, *spos, 0))

tests = {
    """Player 1 starting position: 4
Player 2 starting position: 8""" : [739785, 444356092776315]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)
#
test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#

import time
t1 = time.time_ns()
for i in range(times := 1):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")