import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
from aocl import *
from functional import seq
from fn import _ as l
from math import log10

st=time.time()

day = 7
puzzle = Puzzle(year=2024, day=day)
inp = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()
inp = puzzle.input_data

inp = lines(inp)
sol = 0
for line in inp:
    res, *nums = ints(line)
    if int(seq(nums).make_string("")) < res:
        continue
    for ops in product(["*", "+", ""], repeat=len(nums)-1):
        ops = list(ops)
        s = nums[0]
        for b in nums[1:]:
            if s > res:
                break
            op = ops.pop()
            match op:
                case "*":
                    s *= b
                case "+":
                    s += b
                case "":
                    s = s * 10**(1+int(log10(b))) + b
        if s == res:
            sol += res
            break


print(f"Solution: {sol}\n")
# submit(sol)

print("----%.2f s----"%(time.time()-st))
