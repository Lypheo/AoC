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
day = 21
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = inp.splitlines()
    monkeys = {}
    for l in inp:
        m, op = l.split(": ")
        if not any(s in op for s in "+*-/"):
            op = int(op)
        else:
            op = [op[:4], op[5], op[7:]]
        monkeys[m] = op
    curr = monkeys["root"]
    def calc(exp):
        if not isinstance(exp, int):
            m1, op, m2 = exp
            if op == "+":
                return calc(monkeys[m1]) + calc(calc(monkeys[m2]))
            elif op == "-":
                return calc(monkeys[m1]) - calc(monkeys[m2])
            elif op == "/":
                return int(calc(monkeys[m1]) / calc(monkeys[m2]))
            else:
                return int(calc(monkeys[m1]) * calc(monkeys[m2]))
        else:
            return exp

    return calc(monkeys["root"])

def solve_b(inp=input_data):
    inp = inp.splitlines()
    monkeys = {}
    for l in inp:
        m, op = l.split(": ")
        if not any(s in op for s in "+*-/"):
            op = int(op)
        else:
            op = (op[:4], op[5], op[7:])
        monkeys[m] = op
    monkeys["root"] = (monkeys["root"][0], "==", monkeys["root"][2])
    monkeys["humn"] = "x"

    @functools.cache
    def calc(exp):
        if isinstance(exp, tuple):
            m1, op, m2 = exp
            op1, op2 = calc(monkeys[m1]), calc(monkeys[m2])
            if not all(isinstance(x, int) for x in [op1, op2]):
                return f"({op1}{op}{op2})"
            if op == "+":
                return calc(monkeys[m1]) + calc(monkeys[m2])
            elif op == "-":
                return calc(monkeys[m1]) - calc(monkeys[m2])
            elif op == "/":
                return int(calc(monkeys[m1]) / calc(monkeys[m2]))
            elif op == "*":
                return int(calc(monkeys[m1]) * calc(monkeys[m2]))
            else:
                return int(calc(monkeys[m1]) == calc(monkeys[m2]))
        else:
            return exp
    eq = calc(monkeys["root"]).split("==") # to be pasted into https://www.wolframalpha.com/calculators/equation-solver-calculator
    return eq


tests = {
    """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""" : [152, 301]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

test(tests, solve_b, 1)
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