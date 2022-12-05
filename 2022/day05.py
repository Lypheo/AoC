import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 5
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
    stacksr, moves = inp.split("\n\n")
    stacks  = [None]*9
    for l in stacksr.split("\n")[:-1]:
        for i in range(1, 36, 4):
            if l[i] != " ":
                assert l[i].isupper()
                if stacks[i//4] == None:
                    stacks[i//4] = []
                stacks[i//4] = [l[i]] + stacks[i//4]
    print(stacks)
    for m in moves.split("\n"):
        ds = [int(x) for x in re.findall(r"\d+", m)]
        for i in range(ds[0]):
            item = stacks[ds[1]-1].pop()
            stacks[ds[2]-1].append(item)
    pprint(stacks)
    return "".join([stack[-1] for stack in stacks])
#
def solve_b(inp=input_data):
    stacksr, moves = inp.split("\n\n")
    stacks  = [None]*9
    for l in stacksr.split("\n")[:-1]:
        for i in range(1, 36, 4):
            if l[i] != " ":
                assert l[i].isupper()
                if stacks[i//4] == None:
                    stacks[i//4] = []
                stacks[i//4] = [l[i]] + stacks[i//4]
    print(stacks)
    for m in moves.split("\n"):
        ds = [int(x) for x in re.findall(r"\d+", m)]
        item = stacks[ds[1]-1][-ds[0]:]
        for i in range(ds[0]):
            stacks[ds[1]-1].pop()
        stacks[ds[2]-1].extend(item)
    pprint(stacks)
    return "".join([stack[-1] for stack in stacks])
#

tests = {
    """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""" : ["CMZ", ]
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