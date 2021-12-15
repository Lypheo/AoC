import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 14
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
    e, rules = inp.split("\n\n")
    rules = {r.split(" -> ")[0] : r.split(" -> ")[1] for r in rules.split("\n")}
    for _ in range(10):
        newe = e[0]
        for i in range(len(e)-1):
            s = e[i:i+2]
            if s in rules:
                newe += rules[s] + s[1]
            else:
                newe += s
        e = newe
    cnts = sorted(e.count(x) for x in e)
    return cnts[-1]-cnts[0]


def solve_b(inp=input_data):
    e, rules = inp.split("\n\n")
    rules = {r.split(" -> ")[0] : r.split(" -> ")[1] for r in rules.split("\n")}
    chars = set(e).union(set(rules.values()))
    combs = {c1+c2 : e.count(c1+c2) for c1 in chars for c2 in chars}
    for _ in range(40):
        for k,v in combs.copy().items():
            combs[k] -= v
            a, b = k[0] + rules[k], rules[k] + k[1]
            combs[a] += v
            combs[b] += v

    cnts = dd(int)
    for k,v in combs.items():
        cnts[k[1]] += v
    cnts[e[0]] += 1
    return max(cnts.values())-min(cnts.values())


tests = {
    """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""" : [1588, 2188189693529]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

test(tests, solve_b, 1)
# b = solve_b()
# if b:
#     print(f"Part 2: {b}")
#     submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
import time
t1 = time.time_ns()
for i in range(times := 1000):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")