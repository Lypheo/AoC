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

day = 15
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def line_intersection(line1, line2):
    xdiff = complex(line1[0].real - line1[1].real, line2[0].real - line2[1].real)
    ydiff = complex(line1[0].imag - line1[1].imag, line2[0].imag - line2[1].imag)

    def det(a, b):
        return a.real * b.imag - a.imag * b.real

    div = det(xdiff, ydiff)
    if div == 0:
        # lines do not intersect
        return False

    d = complex(det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return complex(x, y)

def solve_a(inp=input_data, test = False):
    yrow = (2000000 if not test else 10)
    inp = inp.splitlines()
    sensors = {}
    ivs = []
    for line in inp:
        sensor, beacon = line[10:].split(":")
        beacon = beacon.split(" at ")[1]
        sensor = complex(*[int(x.split("=")[1]) for x in sensor.split(", ")])
        beacon = complex(*[int(x.split("=")[1]) for x in beacon.split(", ")])
        sensors[sensor] = beacon
    for sensor, beacon in sensors.items():
        d = mh_dist(sensor, beacon)
        ydiff = yrow - sensor.imag
        if ydiff > d:
            continue
        x = d - abs(ydiff)
        iv = (int(sensor.real - x), int(sensor.real + x))
        ivs.append(iv)

    bs = set(b.real for b in sensors.values() if b.imag == yrow)
    out = 0
    ivs = sorted(ivs, key = lambda iv: iv[0])
    laste = ivs[0][0]-1
    for i in range(len(ivs)):
        s,e = ivs[i]
        if e <= laste:
            continue
        s = max(s, laste + 1)
        out +=  e - s + 1
        out -= int(any(s <= b <= e for b in bs))
        laste = e

    return out

def solve_b(inp=input_data, test = False):
    inp = inp.splitlines()
    ds = {}
    for line in inp:
        sensor, beacon = line[10:].split(":")
        beacon = beacon.split(" at ")[1]
        sensor = complex(*[int(x.split("=")[1]) for x in sensor.split(", ")])
        beacon = complex(*[int(x.split("=")[1]) for x in beacon.split(", ")])
        ds[sensor] = mh_dist(sensor, beacon)

    pairs = []
    for (s1, d1), (s2, d2) in combinations(ds.items(), 2):
        if mh_dist(s1, s2) == d1 + d2 + 2:
            pairs.append((s1, s2))

    for (s1, s2), (s3, s4) in combinations(pairs, 2):
        #        ##S##
        #         ###d#
        #          #d#S#
        #             #
        # basic idea: find the diagonals ("d" in the drawing above) between 2 adjacent sensor circles
        # (adjacent = seperated by a line of width 1)
        # compute the intersection of the diagonals for all pairs of pairs of adjacent sensor border circles
        # if it exists, it must contain a beacon, but it can’t be a known beacon because then its sensor would have to be on top of it
        s1, s2 = sorted([s1,s2], key= lambda s: s.real)
        s3, s4 = sorted([s3,s4], key= lambda s: s.real)
        diags = []
        for s, os in zip([s1, s3], [s2, s4]):
            d = ds[s] + 1
            od = ds[os] + 1
            e = complex(s.real + d, s.imag)
            st = complex(os.real - od, os.imag)
            diags.append([st, e])

        b = line_intersection(*diags)
        if b != False:
            return b.real * 4000000 + b.imag

tests = {
    """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""" : [26, 56000011]
}

test(tests, lambda inp: solve_a(inp, True), 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

test(tests, lambda inp: solve_b(inp, True), 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#

import time
t1 = time.time_ns()
for i in range(times := 20):
    # solve_b()
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")