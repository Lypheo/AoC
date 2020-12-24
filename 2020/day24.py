import math
import time
from datetime import datetime
import time
import functools, itertools, collections, re
from math import ceil, prod, gcd
from collections import defaultdict
cprod = itertools.product

from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 24
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\nInput:\n{i}\nExpected output:\n    {o}\nActual output:\n    ", end="")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    tiles = [re.findall("(se|sw|ne|nw|w|e)", t) for t in inp.split("\n")]
    floor = defaultdict(bool)
    mp = {"ne": (0, 1), "e": (1, 0), "se": (1, -1), "sw": (0, -1), "w": (-1, 0), "nw": (-1, 1)}
    vadd = lambda v1, v2: (v1[0]+v2[0], v1[1] + v2[1])
    for t in tiles:
        pos = functools.reduce(vadd, map(mp.get, t))
        floor[pos] = not floor[pos]

    return sum(floor.values())

def solve_b(inp=input_data):
    tiles = [re.findall("(se|sw|ne|nw|w|e)", t) for t in inp.split("\n")]
    floor = defaultdict(bool)
    mp = {"ne": (0, 1), "e": (1, 0), "se": (1, -1), "sw": (0, -1), "w": (-1, 0), "nw": (-1, 1)}
    vadd = lambda v1, v2: (v1[0]+v2[0], v1[1] + v2[1])
    for t in tiles:
        pos = functools.reduce(vadd, map(mp.get, t))
        floor[pos] = not floor[pos]

    for i in range(100):
        for pos, black in floor.copy().items():
            adj = [vadd(pos, dir) for dir in mp.values()]
            for p in adj:
                floor[p]

        floor_cpy = floor.copy()
        for pos, black in floor.copy().items():
            adj_blacks = sum(floor_cpy[vadd(pos, dir)] for dir in mp.values())
            if black and (adj_blacks == 0 or adj_blacks > 2):
                floor[pos] = False
            elif not black and adj_blacks == 2:
                floor[pos] = True

    return sum(floor.values())

tests = {
    """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""": (10, 2208)
}


# a = solve_a()
# print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)
#
# b = solve_b()
# print(f"Part 2: {b}")
test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")


#
# t1 = time.time_ns()
# for i in range(times := 1):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")