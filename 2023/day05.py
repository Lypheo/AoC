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
day = 5
puzzle = Puzzle(year=2023, day=day)
inp = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip()
inp = puzzle.input_data

# p1

# oinp = puzzle.input_data
# inp = lines(oinp)
# res = 0
# seeds = ints(inp[0].split(": ")[1])
#
# map_blocks = blocks(oinp)
# maps = []
# for mb in map_blocks:
#     ranges = mb.split("\n")[1:]
#     maps.append([])
#     for r in ranges:
#         r = ints(r)
#         maps[-1].append(r)
#
# def find(seed, m):
#     for dest, src, length in m:
#         if src <= seed < src + length:
#             return seed - src + dest
#     return seed
#
# locs = []
# for s in seeds:
#     loc = s
#     for m in maps:
#         loc = find(loc, m)
#     locs.append(loc)
#
# res = min(locs)
# print(f"Solution: {res}\n")

# p2

seeds = ints(inp.splitlines()[0].split(": ")[1])
seed_ranges = [(s,s+l-1) for s, l in zip(seeds[::2], seeds[1::2])]
map_blocks = blocks(inp)

maps = []
for mb in map_blocks[1:]:
    ranges = []
    for r in mb.split("\n")[1:]:
        r = tuple(ints(r))
        ranges.append(r)
    maps.append(ranges)

for m in maps:
    new_ranges = []
    while seed_ranges:
        s, e = seed_ranges.pop()
        for dst_start, src_start, length in m:
            src_end = src_start + length - 1
            offset = dst_start - src_start
            if src_start <= s <= src_end:
                if e > src_end:
                    new_ranges.append((s + offset, src_end + offset))
                    seed_ranges.append((src_end + 1, e))
                else:
                    new_ranges.append((s + offset, e + offset))
                break
            elif src_start <= e <= src_end:
                seed_ranges.append((s, src_start - 1))
                new_ranges.append((src_start + offset, e + offset))
                break
        else:
            new_ranges.append((s, e))
    seed_ranges = new_ranges

res = min(s for s,e in seed_ranges)
print(f"Solution: {res}\n")

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")