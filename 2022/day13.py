import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 13
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
    pairs = inp.split("\n\n")
    cnt = 0
    def right_order(a, b):
        # print(a,b)
        if isinstance(a, int) and isinstance(b, int):
            return a - b
        elif isinstance(a, list) and isinstance(b, list):
            for p, q in zip_longest(a,b, fillvalue=None):
                if p != None and q == None:
                    return 1
                elif p == None and q != None:
                    return -1
                cmp = right_order(p, q)
                if cmp != 0:
                    return cmp
            return 0
        else:
            a = [a] if isinstance(a, int) else a
            b = [b] if isinstance(b, int) else b
            return right_order(a, b)

    for i, pair in enumerate(pairs):
        p1, p2 = map(eval, pair.split("\n"))
        print(p1, p2, right_order(p1, p2), cnt)
        cnt += i + 1 if right_order(p1, p2) < 0 else 0
    return cnt

def solve_b(inp=input_data):
    pairs = inp.split("\n\n")
    pairs.append("""[[2]]
[[6]]""")
    def right_order(a, b):
        # print(a,b)
        if isinstance(a, int) and isinstance(b, int):
            return a - b
        elif isinstance(a, list) and isinstance(b, list):
            for p, q in zip_longest(a,b, fillvalue=None):
                if p != None and q == None:
                    return 1
                elif p == None and q != None:
                    return -1
                cmp = right_order(p, q)
                if cmp != 0:
                    return cmp
            return 0
        else:
            a = [a] if isinstance(a, int) else a
            b = [b] if isinstance(b, int) else b
            return right_order(a, b)

    from functools import cmp_to_key
    packets = []
    for i, pair in enumerate(pairs):
        p1, p2 = map(eval, pair.split("\n"))
        packets.extend([p1,p2])
    ordered = sorted(packets, key=cmp_to_key(right_order))
    return (ordered.index([[2]])+1) * (ordered.index([[6]])+1)


tests = {
    """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""" : [13, 140]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)
#
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