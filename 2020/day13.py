import math
import time
from datetime import datetime
import time
import functools, itertools, collections, re
from math import ceil, prod, gcd

import numpy as np
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 13
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\nInput:\n{i}\nExpected output:\n    {o}\nActual output:\n    ", end="")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    t, bs = inp.split("\n")
    t = int(t); bs = [int(x) for x in bs.split(",") if x != "x"]
    r = min((( (ceil(t/b)*b) % t, b ) for b in bs), key = lambda x: x[0])
    return r[0] * r[1]


def chinese_remainder(a, n): # courtesy of rosetta code lmao
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def solve_b(inp=input_data):
    bs = [(r, int(m)) for r, m in enumerate(inp.split("\n")[1].split(",")) if m != "x"]
    M = prod(m for r, m in bs)
    x = chinese_remainder(*zip(*bs))
    """
    we’re looking for the solution x of the system of congruences given by
    x = -r_i mod -m_i         for all 1 <= i <= len(bs)
    
    However, the CRT only applies for m_i greater than 1, so we instead look for the solution to
    -x = r_i mod m_i         for all 1 <= i <= len(bs)
    which is equivalent by the definition of congruence.
    
    Thus, -x is one solution, but not the smallest. Since CRT holds that -(x + kM) = -x - kM = -x + kM are solutions too, -x % M will be the smallest one.
    """
    return -x % M

tests = {
"""939
7,13,x,x,59,x,31,19""": (295,1068781),
"""12
17,x,13,19""" : (3417,),
"""12
67,7,59,61""" : (754018,),
"""12
67,x,7,59,61""" : (779210,),
"""12
67,7,x,59,61""": (1261476,),
"""21
1789,37,47,1889""": (1202161486,)
}


a = solve_a()
print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

b = solve_b()
print(f"Part 2: {b}")
test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")
#
# t1 = time.time_ns()
# for i in range(times := 5):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")