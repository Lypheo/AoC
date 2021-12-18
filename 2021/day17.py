import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 17
puzzle = Puzzle(year=2021, day=day)
input_data = "target area: x=195..238, y=-93..-67"

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
    inp = inp.split(", ")
    tx = [int(x) for x in inp[0].split("=")[1].split("..")]
    ty = [int(x) for x in inp[1].split("=")[1].split("..")]
    vs = {}
    for xv in range(1, tx[1]+1):
        for yv in range(ty[0], tx[1]):
            dx, dy = xv, yv
            x,y = 0,0
            mh = 0
            while x <= tx[1] and y >= ty[0]:
                x += dx
                y += dy
                mh = max(y, mh)
                dx  = dx + (1 if x < 0 else -1) if dx != 0 else 0
                dy -= 1
                if x >= tx[0] and y >= ty[0] and x <= tx[1] and y <= ty[1]:
                    vs[(xv,yv)] = mh
                    break

    print((-ty[0] ** 2 + tx[0]) / 2)
    return max(vs.values())

def solve_b(inp=input_data):
    inp = inp.split(", ")
    tx = [int(x) for x in inp[0].split("=")[1].split("..")]
    ty = [int(x) for x in inp[1].split("=")[1].split("..")]
    vs = {}
    for xv in range(1, tx[1]+1):
        xr = (xv**2 + xv) / 2
        for yv in range(ty[0], tx[1]):
            dx, dy = xv, yv
            x,y = 0,0
            mh = 0
            while x <= tx[1] and y >= ty[0]:
                x += dx
                y += dy
                mh = max(y, mh)
                dx  = dx + (1 if x < 0 else -1) if dx != 0 else 0
                dy -= 1
                if x >= tx[0] and y >= ty[0] and x <= tx[1] and y <= ty[1]:
                    vs[(xv,yv)] = mh
                    break

    return len(vs)

tests = {
    # "target area: x=20..30, y=-10..-5" : [45, 112]
}

# test(tests, solve_a, 0)
a = solve_a()
print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

# test(tests, solve_b, 1)
# b = solve_b("target area: x=34..67, y=-215..-186")
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#

# import time
# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")