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
day = 3
puzzle = Puzzle(year=2023, day=day)
inp = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()
inp = puzzle.input_data


grid = dict()
inp = lines(inp)
for y, line in enumerate(inp):
    for x, c in enumerate(line):
        grid[complex(x, y)] = c

res = 0
# for y, line in enumerate(inp):
#     maxx = -1
#     for x, c in enumerate(line):
#         if x <= maxx:
#             continue
#         ns = [grid.get(n + complex(x,y), "") for n in nbd(complex(x,y))]
#         if c.isdigit() and any(k != "." and not k.isdigit() for k in ns):
#             num = ""
#             x2 = x
#             maxx = x
#             while grid.get(complex(x2, y), "").isdigit():
#                 num = grid[complex(x2, y)] + num
#                 x2 -= 1
#             x2 = x+1
#             while grid.get(complex(x2, y), "").isdigit():
#                 num += grid[complex(x2, y)]
#                 x2 += 1
#                 maxx = x2
#             res += int(num)

#p1
for y, line in enumerate(inp):
    num = ""
    for x, c in enumerate(line + "."):
        if c.isdigit():
            num += c
        elif num:
            nbs = {n for x2 in sr(x-1, x-len(num)-1) for n in nbd(complex(x2,y))} - set(sr(x-1, x-len(num)-1))
            nbc = [grid.get(k, ".") for k in nbs]
            # print(x, y, num, [n + complex(x2,y) for x2 in sr(x-1, x-len(num)-1) for n in nbd(complex(x2,y))])
            if any(not k.isdigit() and k != "." for k in nbc):
                res += int(num)
            num = ""
#p2
for y, line in enumerate(inp):
    for x, c in enumerate(line + "."):
        if c == "*":
            nbs = nbdl(complex(x, y))
            numps = [p for p in nbs if grid.get(p, "").isdigit()]
            numps.sort(key=lambda k: mh_dist(k, complex(x-1, y-1)))
            for i, p in enumerate(numps):
                while p + 1 in numps:
                    numps.remove(p + 1)
                    p += 1
            print(x, y, numps)
            if len(numps) == 2:
                r = 1
                for p in numps:
                    op = p
                    num = ""
                    while grid.get(p, "").isdigit():
                        num = grid[p] + num
                        p -= 1
                    p = op + 1
                    while grid.get(p, "").isdigit():
                        num += grid[p]
                        p += 1
                    r *= int(num)
                res += r





print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")