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

mh_dist = lambda a,b: int(abs(a.real - b.real) + abs(a.imag - b.imag))

def sr(a, b=None, step=1, inc=False): # signed range
    if b == None:
        start, end = 0, a
    else:
        start, end = a, b
    if inc:
        end += 1 if end >= start else -1
    return range(start, end, step if end >= start else -step)

def ip(st, e): # interpolate complex numbers
    diff = e - st
    rng = []
    if diff.real == 0:
        rng = [complex(st.real, st.imag + y) for y in sr(int(diff.imag), inc=True)]
    elif diff.imag == 0:
        rng = [complex(st.real + x, st.imag) for x in sr(int(diff.real), inc=True)]
    elif abs(diff.imag) > abs(diff.real):
        for x in sr(int(diff.real), inc=True):
            rng.append(complex(st.real + x, st.imag + x * diff.imag / diff.real))
    else:
        for y in sr(int(diff.imag), inc=True):
            rng.append(complex(st.real + y * diff.real / diff.imag, st.imag + y))
    return rng

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
        s1, s2 = sorted([s1,s2], key= lambda s: s.real)
        s3, s4 = sorted([s3,s4], key= lambda s: s.real)
        borders = []
        for s, os in zip([s1, s3], [s2, s4]):
            d = ds[s] + 1
            od = ds[os] + 1
            e = complex(s.real + d, s.imag)
            st = complex(os.real - od, os.imag)
            borders.append(set(ip(st, e)))
        beacon = set.intersection(*borders)
        if len(beacon) == 1:
            b = beacon.pop()
            # if not any(mh_dist(b, s) <= ds[s] for s in ds.keys()):
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