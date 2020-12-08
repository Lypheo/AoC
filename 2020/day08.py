import time
from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 8
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    ops = [(x.split()[0], int(x.split()[1])) for x in inp.split("\n")]
    visited = []
    acc = 0
    i = 0
    while i < len(ops):
        visited.append(i)
        if ops[i][0] == "jmp":
            i = i + ops[i][1]
            if i in visited:
                return acc
            continue
        elif ops[i][0] == "acc":
            acc += ops[i][1]
        i += 1

def solve_b(inp=input_data):
    p = [[x.split()[0], int(x.split()[1])] for x in inp.split("\n")]
    def loops(ops):
        visited = []
        acc = 0
        i = 0
        while i < len(ops):
            visited.append(i)
            if ops[i][0] == "jmp":
                i = i + ops[i][1]
                if i in visited:
                    return True, None
                continue
            elif ops[i][0] == "acc":
                acc += ops[i][1]
            i += 1
        return i != len(ops), acc

    for i in range(len(p)):
        newp = [e.copy() for e in p]
        if p[i][0] == "nop":
            newp[i][0] = "jmp"
        elif p[i][0] == "jmp":
            newp[i][0] = "nop"
        else:
            continue
        ret = loops(newp)
        if not ret[0]:
            return ret[1]

# a = solve_a(tests[0])
# print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

tests = {
    """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""": (8,)
}

b = solve_b()
print(f"Part 2: {b}")
# test(tests, solve_b)
submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 5):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")
#
# t1 = time.time_ns()
# for i in range(times := 5):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")