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
from functional import seq
from fn import _ as l
from pyperclip import copy

st=time.time()

puzzle = Puzzle(year=2024, day=24)
inp = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
""".strip()
inp = puzzle.input_data

res = 0
init, gatesR = blocks(inp)
init, gatesR = lines(init), lines(gatesR)
outputs = {line.split(": ")[0]: int(line.split(": ")[1]) for line in init}
gates = []
for line in gatesR:
    line = line.split()
    gates.append((line[1], line[0], line[2], line[4]))
def compute(outputs, gates):
    while True:
        last = len(outputs)
        for type, in1, in2, out in gates:
            if in1 in outputs and in2 in outputs:
                match type:
                    case "AND":
                        outputs[out] = outputs[in1] & outputs[in2]
                    case "OR":
                        outputs[out] = outputs[in1] | outputs[in2]
                    case "XOR":
                        outputs[out] = outputs[in1] ^ outputs[in2]
        if len(outputs) == last: break
    return outputs

def calc(Wires, letter):
    wires = {k:v for k,v in Wires.items() if k.startswith(letter)}
    dec = [0]*len(wires)
    for wire, val in wires.items():
        dec[int(wire[1:])] = str(val)
    dec = reversed(dec)
    return int("".join(dec), 2)

outputs = compute(outputs, gates)
p1 = calc(outputs, "z")

# vpm: should XOR->(AND,XOR) | is XOR->OR
# qnf: should AND->OR | is AND->(AND,XOR)
# vpm <=> qnf

# z32: should XOR-> | is AND->
# tbt: should z** | is XOR->OR
# tbt <=> z32

# gsd: should z** | is XOR->OR
# z26: should XOR-> | is AND->
# gsd <=> z26

# kth: should z** | is XOR->(AND,XOR)
# z12: should XOR-> | is OR->
# kth <=> z12

for i in range(46):
    if not any(out == f"z{i:02d}" and type == "XOR" for type, in1, in2, out in gates) and i != 45:
        print(f"z{i:02d}")

for type, in1, in2, out in gates:
    if type == "XOR" and not out[0] == "z":
        leadsTo = set(ttype for ttype, iin1, iin2, oout in gates if iin1 == out or iin2 == out)
        if leadsTo != {"AND", "XOR"}:
            print(type, in1, in2, out, leadsTo)
    if type == "AND":
        leadsTo = set(ttype for ttype, iin1, iin2, oout in gates if iin1 == out or iin2 == out)
        if "AND" in leadsTo:
            print("AND to AND:", type, in1, in2, out)

    if type == "XOR" and {in1[0], in2[0]} != {"x", "y"}:
        if out[0] != "z":
            print("WRONG Z:", type, in1, in2, out)

p2 = ",".join(sorted(["vpm", "qnf", "tbt", "z32", "gsd", "z26", "kth", "z12"]))
print(f"Solution: {p1, p2}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")