import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
import sys
sys.path.append("..")
from aocl import *
day = 25
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def dec(l):
    n = 0
    for i, c in enumerate(reversed(l)):
        n += 5**i * {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}[c]
    return n

lut = {v:k for k, v in {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}.items()}

def hp(n):
    if n < 0:
        return hp(-n)
    ans = 0
    while n != 0:
        n //= 5
        ans += 1
    return ans - 1

def enc(num):
    s = dd(int)
    while num != 0:
        p = hp(num)
        f = num // (5**p) + (1 if num < 0 and num % (5**p) else 0)
        co = int(5 * 5**p /2)
        print(num, 5**p, f)
        if num > co:
            s[p+1] += 1
            num -= 5**(p+1)
        elif num < -co:
            s[p+1] -= 1
            num += 5**(p+1)
        else:
            s[p] += f
            num -= 5**(p) * s[p]
    print(s)
    assert all(-2 <= v <= 2 for v in s.values())
    maxp = max(s.keys())
    ans = ""
    for i in sr(maxp, 0, inc=True):
        ans += lut[s.get(i, 0)]
    return ans


def solve_a(inp=input_data):
    inp = inp.splitlines()
    summ = 0
    for l in inp:
        summ += dec(l)

    return enc(summ)



def solve_b(inp=input_data):
    return False

tests = {
    """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""": ["2=-1=0"],

}

# test(tests, solve_a, 0)
a = solve_a()
print(f"Part 1: {a}\n")
submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

# test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")