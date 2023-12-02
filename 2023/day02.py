import time
import functools, itertools, collections, re
from math import prod

from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
import sys
sys.path.append("..")
from aocl import *
day = 2
puzzle = Puzzle(year=2023, day=day)
inp = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()
inp = puzzle.input_data


# inp = lines(inp)
# res = 0
# for i, line in enumerate(inp):
#     impossible = False
#     idx = i+1
#     game = line.split(": ")[1]
#     sets = game.split("; ")
#     for s in sets:
#         bags = {bag.split(" ")[1]:ints(bag)[0] for bag in s.split(", ")}
#         if bags.get("red", 0) > 12 or bags.get("green", 0) > 13 or bags.get("blue", 0) > 14:
#             impossible  = True
#             break
#     if not impossible:
#         res += idx

inp = lines(inp)
res = 0
for i, line in enumerate(inp):
    impossible = False
    idx = i+1
    game = line.split(": ")[1]
    sets = game.split("; ")
    minbags = {"red": 0, "blue": 0, "green": 0}
    for s in sets:
        bags = {bag.split(" ")[1]:ints(bag)[0] for bag in s.split(", ")}
        for k,v in bags.items():
            minbags[k] = max(minbags[k], v)

    res += prod(minbags.values())

# print(f"Solution: {res}\n")
submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")