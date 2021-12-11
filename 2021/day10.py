import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 10
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


error = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
d = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
dr = {v:k for k,v in d.items()}
def solve_a(inp=input_data):
    inp = inp.splitlines()
    s = 0
    for l in inp:
        stack = []
        for c in l:
            if c in d:
                stack.append(c)
            else:
                if dr[c] != stack[-1]:
                    s += error[c]
                    break
                else:
                    stack.pop()

    return s
score = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
def solve_b(inp=input_data):
    inp = inp.splitlines()
    s = []
    for l in inp:
        stack = []
        for c in l:
            if c in d:
                stack.append(c)
            else:
                if dr[c] != stack[-1]:
                    break
                else:
                    stack.pop()
        else:
            ss = 0
            for c in stack[::-1]:
                ss *= 5
                ss += score[d[c]]
            s.append(ss)

    return sorted(s)[len(s)//2]

tests = {
    """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""" : [26397, 288957]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

# test(tests, solve_b, 1)
b = solve_b()
if b:
    print(f"Part 2: {b}")
    # submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#

import time
t1 = time.time_ns()
for i in range(times := 1000):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(times)} ns")