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
day = 24
puzzle = Puzzle(year=2023, day=day)
inp = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".strip()
inp = puzzle.input_data
lower = 200000000000000
upper = 400000000000000
# lower = 7
# upper = 27

inp = lines(inp)
res = 0
hails = []
for line in inp:
    p, v = line.split(" @ ")
    p = [int(x) for x in p.split(", ")]
    v = [int(x) for x in v.split(", ")]
    hails.append((p, v))

for h1, h2 in combinations(hails, 2):
    x1, y1,_  = h1[0]
    x2, y2,_  = h2[0]
    vx1, vy1,_ = h1[1]
    vx2, vy2,_ = h2[1]
    # p1 + v1*t = p2 + v2*u
    # x1 + vx1*t = x2 + vx2*u
    # y1 + vy1*t = y2 + vy2*u
    # (x1-x2 + vx1*t)/vx2 = u
    # y1 + vy1*t = y2 + vy2*((x1-x2 + vx1*t)/vx2)

    # t = (vy_2 (x_2 - x_1) + (y_1 - y_2) vx_2)/(vy_2 vx_1 - vy_1 vx_2) and vy_1 vx_2!=vy_2 vx_1
    if vy1 * vx2 == vy2 * vx1 or (vy1 * vx2 - vy2 * vx1) == 0:
        continue

    t = (vy2 * (x2 - x1) + (y1 - y2) * vx2) / (vy2 * vx1 - vy1 * vx2)
    u = (vy1 * (x1 - x2) + (y2 - y1) * vx1) / (vy1 * vx2 - vy2 * vx1)
    crossx = x1 + t*vx1
    crossy = y1 + t*vy1
    # print(h1, h2, t)
    # print(crossx, crossy)
    if t > 0 and u > 0 and lower <= crossx <= upper and lower <= crossy <= upper:
        # print("inside")
        res += 1


print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")