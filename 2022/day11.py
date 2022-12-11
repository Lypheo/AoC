import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 11
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
    items = []
    ops = []
    tests = []
    for monkey in inp.split("\n\n"):
        monkey = monkey.split("\n")
        op = monkey[2].split("old ")[1].split(" ")
        op[1] = int(op[1]) if op[1] != "old" else "old"
        ops.append(op)
        nt = []
        nt.append(int(monkey[3].split(" ")[-1]))
        nt.append(int(monkey[4].split(" ")[-1]))
        nt.append(int(monkey[5].split(" ")[-1]))
        tests.append(nt)
        items.append([int(x) for x in monkey[1].split(": ")[1].split(", ")])
    counts = [0]*len(ops)
    from copy import deepcopy
    for i in range(20):
        for m in range(len(ops)):
            # print(items)
            for it in deepcopy(items)[m]:
                # print(it)
                wl = it
                if ops[m][0] == "*":
                    wl *= ops[m][1] if ops[m][1] != "old" else wl
                else:
                    wl += ops[m][1] if ops[m][1] != "old" else wl
                wl //= 3
                if wl % tests[m][0] != 0:
                    items[tests[m][2]].append(wl)
                else:
                    items[tests[m][1]].append(wl)
                items[m].pop(0)
                counts[m] += 1

    counts = sorted(counts)
    return counts[-1] * counts[-2]

def solve_b(inp=input_data):
    items = []
    ops = []
    tests = []
    for monkey in inp.split("\n\n"):
        monkey = monkey.split("\n")
        op = monkey[2].split("old ")[1].split(" ")
        op[1] = int(op[1]) if op[1] != "old" else "old"
        ops.append(op)
        nt = []
        nt.append(int(monkey[3].split(" ")[-1]))
        nt.append(int(monkey[4].split(" ")[-1]))
        nt.append(int(monkey[5].split(" ")[-1]))
        tests.append(nt)
        items.append([int(x) for x in monkey[1].split(": ")[1].split(", ")])
    counts = [0]*len(ops)
    divs = [t[0] for t in tests]
    items = [[[it % div for div in divs] for it in its] for its in items]
    from copy import deepcopy
    for i in range(10000):
        for m in range(len(ops)):
            for prev_wl in deepcopy(items)[m]:
                worrylevel = []
                for k, div in zip(prev_wl, divs):
                    # in the case of old * old, we can square the remainder cuz a^k = b^k (mod n). old + old doesn’t happen in my input so disregard that case
                    operand = ops[m][1] if ops[m][1] != "old" else k
                    # this works because a + k = b + k (mod n) and a * k = b * k (mod n)
                    if ops[m][0] == "*":
                        worrylevel.append((k * operand) % div)
                    else:
                        worrylevel.append((k + operand) % div)

                if worrylevel[m] != 0:
                    items[tests[m][2]].append(worrylevel)
                else:
                    items[tests[m][1]].append(worrylevel)
                items[m].pop(0)
                counts[m] += 1

    counts = sorted(counts)
    return counts[-1] * counts[-2]

tests = {
    """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""": [10605, 2713310158]
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