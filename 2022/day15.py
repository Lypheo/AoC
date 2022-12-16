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
    print(ivs)
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
    radii = {}
    for line in inp:
        sensor, beacon = line[10:].split(":")
        beacon = beacon.split(" at ")[1]
        sensor = complex(*[int(x.split("=")[1]) for x in sensor.split(", ")])
        beacon = complex(*[int(x.split("=")[1]) for x in beacon.split(", ")])
        radii[sensor] = mh_dist(sensor, beacon)

    pairs = []
    for (s1, d1), (s2, d2) in combinations(radii.items(), 2):
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
        for sensor_a, sensor_b in zip([s1, s3], [s2, s4]):
            r_a = radii[sensor_a] + 1
            r_b = radii[sensor_b] + 1
            end = complex(sensor_a.real + r_a, sensor_a.imag)
            start = complex(sensor_b.real - r_b, sensor_b.imag)
            diags.append([start, end])

        b = line_intersection(*diags)
        if b != False:
            return int(round(b.real) * 4000000 + round(b.imag))

tests = {
#     """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""" : [26, 56000011],
    """Sensor at x=3729579, y=1453415: closest beacon is at x=4078883, y=2522671
Sensor at x=3662668, y=2749205: closest beacon is at x=4078883, y=2522671
Sensor at x=257356, y=175834: closest beacon is at x=1207332, y=429175
Sensor at x=2502777, y=3970934: closest beacon is at x=3102959, y=3443573
Sensor at x=24076, y=2510696: closest beacon is at x=274522, y=2000000
Sensor at x=3163363, y=3448163: closest beacon is at x=3102959, y=3443573
Sensor at x=1011369, y=447686: closest beacon is at x=1207332, y=429175
Sensor at x=3954188, y=3117617: closest beacon is at x=4078883, y=2522671
Sensor at x=3480746, y=3150039: closest beacon is at x=3301559, y=3383795
Sensor at x=2999116, y=3137910: closest beacon is at x=3102959, y=3443573
Sensor at x=3546198, y=462510: closest beacon is at x=3283798, y=-405749
Sensor at x=650838, y=1255586: closest beacon is at x=274522, y=2000000
Sensor at x=3231242, y=3342921: closest beacon is at x=3301559, y=3383795
Sensor at x=1337998, y=31701: closest beacon is at x=1207332, y=429175
Sensor at x=1184009, y=3259703: closest beacon is at x=2677313, y=2951659
Sensor at x=212559, y=1737114: closest beacon is at x=274522, y=2000000
Sensor at x=161020, y=2251470: closest beacon is at x=274522, y=2000000
Sensor at x=3744187, y=3722432: closest beacon is at x=3301559, y=3383795
Sensor at x=2318112, y=2254019: closest beacon is at x=2677313, y=2951659
Sensor at x=2554810, y=56579: closest beacon is at x=3283798, y=-405749
Sensor at x=1240184, y=897870: closest beacon is at x=1207332, y=429175
Sensor at x=2971747, y=2662873: closest beacon is at x=2677313, y=2951659
Sensor at x=3213584, y=3463821: closest beacon is at x=3102959, y=3443573
Sensor at x=37652, y=3969055: closest beacon is at x=-615866, y=3091738
Sensor at x=1804153, y=1170987: closest beacon is at x=1207332, y=429175""" : [4827924, 12977110973564],
    """Sensor at x=3291456, y=3143280: closest beacon is at x=3008934, y=2768339
Sensor at x=3807352, y=3409566: closest beacon is at x=3730410, y=3774311
Sensor at x=1953670, y=1674873: closest beacon is at x=2528182, y=2000000
Sensor at x=2820269, y=2810878: closest beacon is at x=2796608, y=2942369
Sensor at x=3773264, y=3992829: closest beacon is at x=3730410, y=3774311
Sensor at x=2913793, y=2629579: closest beacon is at x=3008934, y=2768339
Sensor at x=1224826, y=2484735: closest beacon is at x=2528182, y=2000000
Sensor at x=1866102, y=3047750: closest beacon is at x=1809319, y=3712572
Sensor at x=3123635, y=118421: closest beacon is at x=1453587, y=-207584
Sensor at x=2530789, y=2254773: closest beacon is at x=2528182, y=2000000
Sensor at x=230755, y=3415342: closest beacon is at x=1809319, y=3712572
Sensor at x=846048, y=51145: closest beacon is at x=1453587, y=-207584
Sensor at x=3505756, y=3999126: closest beacon is at x=3730410, y=3774311
Sensor at x=2506301, y=3745758: closest beacon is at x=1809319, y=3712572
Sensor at x=1389843, y=957209: closest beacon is at x=1453587, y=-207584
Sensor at x=3226352, y=3670258: closest beacon is at x=3730410, y=3774311
Sensor at x=3902053, y=3680654: closest beacon is at x=3730410, y=3774311
Sensor at x=2573020, y=3217129: closest beacon is at x=2796608, y=2942369
Sensor at x=3976945, y=3871511: closest beacon is at x=3730410, y=3774311
Sensor at x=107050, y=209321: closest beacon is at x=1453587, y=-207584
Sensor at x=3931251, y=1787536: closest beacon is at x=2528182, y=2000000
Sensor at x=1637093, y=3976664: closest beacon is at x=1809319, y=3712572
Sensor at x=2881987, y=1923522: closest beacon is at x=2528182, y=2000000
Sensor at x=3059723, y=2540501: closest beacon is at x=3008934, y=2768339""" : [5564017, 11558423398893]
}

# test(tests, lambda inp: solve_a(inp, False), 0)
a = solve_a()
print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

test(tests, lambda inp: solve_b(inp, False), 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#

import time
t1 = time.time_ns()
for i in range(times := 100):
    # solve_a()
    solve_b()

t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")