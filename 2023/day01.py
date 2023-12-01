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
day = 1
puzzle = Puzzle(year=2023, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = lines(inp)
    c = 0
    for l in inp:
        nums = [x for x in l if x.isnumeric()]

        c += int(f"{nums[0]}{nums[-1]}")
    return c

def solve_b(inp=input_data):
    inp = lines(inp)
    c = 0
    for l in inp:
        # chunks = re.split(f"(one|two|three|four|five|six|seven|eight|nine)", l)
        # newl = ""
        # for chunk in chunks:
        #     for i, s in enumerate("one,two,three,four,five,six,seven,eight,nine".split(",")):
        #         chunk = chunk.replace(s, str(i+1))
        #     newl += chunk

        # newl = ""
        # i = 0
        # while i < len(l):
        #     rl = l[i:]
        #     m = re.match("(one|two|three|four|five|six|seven|eight|nine)", rl)
        #     if m:
        #         d = m.group(0)
        #         for k, s in enumerate("one,two,three,four,five,six,seven,eight,nine".split(",")):
        #             d = d.replace(s, str(k+1))
        #         newl += d
        #         i += len(m.group(0))
        #     else:
        #         newl += rl[0]
        #         i += 1
        firstm = re.match(r".*?(one|two|three|four|five|six|seven|eight|nine|\d)", l).group(1)
        lastm = re.match(r".*?(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)", "".join((reversed(l)))).group(1)
        nums = [firstm, lastm]
        print(l, nums)
        for i, num in enumerate(nums):
            for k, s in enumerate("one,two,three,four,five,six,seven,eight,nine".split(",")):
                num = num.replace(s, str(k+1))
            for k, s in enumerate("eno|owt|eerht|ruof|evif|xis|neves|thgie|enin".split("|")):
                num = num.replace(s, str(k+1))
            c += int(num) * (10 if not i else 1)

    return c

tests = {
    """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""": [142, None],
    """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""": [None, 281]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2023)

test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2023)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")