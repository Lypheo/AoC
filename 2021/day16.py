import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 16
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def parse_packet(p):
    # print("Packet: ", p)
    parsed = {}
    parsed["version"] = int(p[:3], 2)
    parsed["type"] = int(p[3:6], 2)
    b = p[6:]
    l = 6
    if parsed["type"] == 4: # literal
        v = ""
        while b[0] == "1":
            lambda a,b: a*b
            v += b[1:5]
            b = b[5:]
            l += 5
        v += b[1:5]
        b = b[5:]
        l += 5
        parsed["payload"] = int(v, 2)
    else:
        ltid = b[0]
        b = b[1:]
        l += 1
        subps = []
        if int(ltid, 2):
            l += 11
            numsub = int(b[:11], 2)
            subp = b[11:]
            for i in range(numsub):
                pkg, subp = parse_packet(subp)
                subps.append(pkg)
                l += pkg["length"]
            b = subp
        else:
            l += 15
            numbits = int(b[:15], 2)
            l += numbits
            subp = b[15:15+numbits]
            b = b[15+numbits:]
            pkg, subp = parse_packet(subp)
            subps.append(pkg)
            sl = pkg["length"]
            while sl < numbits:
                pkg, subp = parse_packet(subp)
                subps.append(pkg)
                sl += pkg["length"]
        parsed["subps"] = subps
    parsed["length"] = l
    return parsed, b

def solve_a(inp=input_data):
    binary = bin(int(inp, 16))[2:]
    binary = "0"* ((4 - len(binary) % 4) % 4) + binary
    pkg, _ = parse_packet(binary)
    def vs(p):
        return p["version"] + sum(vs(sp) for sp in p["subps"])
    return vs(pkg)

def ev(p):
    match p["type"]:
        case 0:
            return sum(ev(sp) for sp in p["subps"])
        case 1:
            x = 1
            for i in (ev(sp) for sp in p["subps"]):
                x *= i
            return x
        case 2:
            return min(ev(sp) for sp in p["subps"])
        case 3:
            return max(ev(sp) for sp in p["subps"])
        case 4:
            return p["payload"]
        case 5:
            a,b = p["subps"]
            return int(ev(a) > ev(b))
        case 6:
            a,b = p["subps"]
            return int(ev(a) < ev(b))
        case 7:
            a,b = p["subps"]
            return int(ev(a) == ev(b))

def solve_b(inp=input_data):
    binary = bin(int(inp, 16))[2:]
    binary = "0"* ((4 - len(binary) % 4) % 4) + binary
    while inp[0] == "0":
        binary = "0000" + binary
        inp = inp[1:]
    pkg, _ = parse_packet(binary)
    return ev(pkg)


tests = {
    "C200B40A82" : [1,3],
    "04005AC33890" : [1,54],
    "880086C3E88112" : [1,7],
    "CE00C43D881120" : [1,9],
    "D8005AC2A8F0" : [1,1],
    "F600BC2D8F" : [1,0],
    "9C005AC2F8F0" : [1,0],
    "9C0141080250320F1802104A08" : [1,1],
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

# test(tests, solve_b, 1)
b = solve_b()
if b:
    print(f"Part 2: {b}")
    submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")