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

day = 14
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
    lines = inp.split("\n")
    mem = {}
    mask = None
    for l in lines:
        if l.startswith("mask ="):
            mask = re.findall("mask = ([X01]*)", l)[0]
        else:
            loc, val = re.findall("mem\[(\d+)\] = (\d+)", l)[0]
            val = bin(int(val))[2:]
            val = list(val.rjust(len(mask), "0"))
            # print("".join(val))
            for i in range(len(val)):
                if mask[i] != "X":
                    val[i] = mask[i]

            loc, val = int(loc), int("".join(val), 2)
            mem[loc] = val
            print(loc, val)
    return sum(mem.values())

def solve_b(inp=input_data):
    lines = inp.split("\n")
    mem = {}
    mask = None
    for l in lines:
        if l.startswith("mask ="):
            mask = re.findall("mask = ([X01]*)", l)[0]
        else:
            loc, val = re.findall("mem\[(\d+)\] = (\d+)", l)[0]
            val = int(val)
            loc = bin(int(loc))[2:]

            loc = list(loc.rjust(len(mask), "0"))
            for i in range(len(loc)):
                if mask[i] != "0":
                    loc[i] = mask[i]

            loc = "".join(loc)
            c = loc.count("X")
            for i in range(2**c):
                loc2 = loc
                b = bin(i)[2:].rjust(c, "0")
                for d in b:
                    loc2 = loc2.replace("X", d, 1)
                mem[int(loc2, 2)] = val

    return sum(mem.values())

tests = {
# """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0""" : (165, ),
    """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""": (208, )
}


# a = solve_a()
# print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

b = solve_b()
print(f"Part 2: {b}")
# test(tests, solve_b)
submit(b, part="b", day=day, year=2020)

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