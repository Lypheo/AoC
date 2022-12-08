import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from functools import reduce

day = 7
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data
bigboy = open(r"C:\Users\saifu\Downloads\bigboy.txt").read()
def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def solve(inp=input_data, bb = False):
    inp = inp.splitlines()
    tree = {"/" : {}}
    cd = []
    for l in inp:
        if l.startswith("$ cd"):
            d = l.split(" ")[-1]
            if d == "..":
                cd.pop()
            elif d == "/":
                cd = ["/"]
            else:
                cd.append(d)
        elif l.startswith("dir"):
            d = l.split(" ")[-1]
            reduce(lambda t, x: t[x], [tree] + cd)[d] = {}
        elif l.startswith("$ ls"):
            continue
        else:
            size, name = l.split(" ")
            reduce(lambda t, x: t[x], [tree] + cd)[name] = size

    total = 0
    sizes = []
    def calc(p, c):
        if isinstance(c, str):
            return int(c)
        else:
            size = sum(calc(pp, cc) for pp, cc in c.items())
            nonlocal total, sizes
            total += size if size <= 100000 else 0
            sizes.append(size)
            return size

    s = calc("/", tree["/"])
    to_delete = 30000000 - (70000000 - s) if not bb else 700000000  - (3000000000  - s)
    return total, [x for x in sorted(sizes) if x >= to_delete][0]

tests = {
    """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""" : [95437, 24933642]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

# test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
import time
t1 = time.time_ns()
for i in range(times := 1):
    print(solve(bigboy, True))
    # print(solve(input_data, False))
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")
print(f"Time: {(t2-t1)/(times):,} ns")