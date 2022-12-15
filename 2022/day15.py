import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint

day = 15
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data
"Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data, test = False):
    yrow = (2000000 if not test else 10)
    inp = inp.splitlines()
    sensors = {}
    ans = dd(list)
    for line in inp:
        sensor, beacon = line[10:].split(":")
        beacon = beacon.split(" at ")[1]
        sensor = complex(*[int(x.split("=")[1]) for x in sensor.split(", ")])
        beacon = complex(*[int(x.split("=")[1]) for x in beacon.split(", ")])
        sensors[sensor] = beacon
    for sensor, beacon in sensors.items():
        diff = sensor - beacon
        d = sum(int(abs(x)) for x in [diff.imag, diff.real])
        print(sensor)
        for y in range(d+1):
            x = d - y
            iv = (int(sensor.real - x), int(sensor.real + x))
            ivs = []
            for b in sensors.values():
                by = int(b.imag)
                if by in range(iv[0], iv[1]+1):
                    ivs.extend([(iv[0], by-1), (by+1, iv[1])])
            if not ivs:
                ivs = [iv]
            if sensor.imag + y == yrow:
                ans[sensor.imag + y].extend(ivs)
            if sensor.imag - y == yrow:
                ans[sensor.imag - y].extend(ivs)

    out = set()
    for iv in ans[yrow]:
        out.update(range(iv[0], iv[1]))
    return len(out)

def solve_b(inp=input_data, test = False):
    wind = (4000000 if not test else 20)
    inp = inp.splitlines()
    sensors = {}
    for line in inp:
        sensor, beacon = line[10:].split(":")
        beacon = beacon.split(" at ")[1]
        sensor = complex(*[int(x.split("=")[1]) for x in sensor.split(", ")])
        beacon = complex(*[int(x.split("=")[1]) for x in beacon.split(", ")])
        sensors[sensor] = beacon
    ds = {}
    mh_dist = lambda a,b: int(abs(a.real - b.real) + abs(a.imag - b.imag))
    for sensor, beacon in sensors.items():
        ds[sensor] = mh_dist(sensor, beacon)

    pairs = []
    for (s1, d1), (s2, d2) in combinations(ds.items(), 2):
        if mh_dist(s1, s2) == d1 + d2 + 2:
            pairs.append((s1, s2))

    for (s1, s2), (s3, s4) in combinations(pairs, 2):
    # for ss in combinations(sensors.keys(), 4):
        ss = [s1, s2, s3, s4]
        borders = []
        for s in ss:
            d = ds[s] + 1
            border = set()
            border.update(complex(s.real + x, s.imag + (d-abs(x))) for x in range(-d, d+1))
            border.update(complex(s.real + x, s.imag - (d-abs(x))) for x in range(-d, d+1))
            borders.append(border)
        beacon = set.intersection(*borders)
        if len(beacon) == 1:
            b = beacon.pop()
            if not any(mh_dist(b, s) <= ds[s] for s in sensors.keys()):
                print(b, ss)
                return b.real * 4000000 + b.imag


        # midp1_raw = (s2 - s1)/ 2 + s1
        # midp1 = complex(ceil(midp1_raw.real), ceil(midp1_raw.imag))
        # print(midp1, s1, s2)
        # for dir in (complex(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)):
        #     adj_pair = (midp1 + dir, midp1 - dir)
        #     if mh_dist(adj_pair[0], s3) == ds[s3] and mh_dist(adj_pair[1], s4) == ds[s4]:
        #         return midp1.real * 4000000 + midp1.imag

        # p1_raw = (s2 - s1)/ 2 + s1
        # p1 = complex(ceil(p1_raw.real), ceil(p1_raw.imag))
        # p2_raw = (s4 - s3)/ 2 + s3
        # p2 = complex(ceil(p2_raw.real), ceil(p2_raw.imag))
        # if p1 == p2:
        #     print(p1)
        #     return p1.real * 4000000 + p1.imag
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

# test(tests, lambda inp: solve_a(inp, True), 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

# test(tests, lambda inp: solve_b(inp, True), 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
import time
t1 = time.time_ns()
for i in range(times := 1):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")