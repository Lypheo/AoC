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

init, gatesR = blocks(inp)
init, gatesR = lines(init), lines(gatesR)
outputs = {line.split(": ")[0]: int(line.split(": ")[1]) for line in init}
gates = []
for line in gatesR:
    line = line.split()
    gates.append((line[1], line[0], line[2], line[4]))

target = len(outputs) + len(gates)
while len(outputs) != target:
    for type, in1, in2, out in gates:
        if in1 in outputs and in2 in outputs:
            match type:
                case "AND":
                    outputs[out] = outputs[in1] & outputs[in2]
                case "OR":
                    outputs[out] = outputs[in1] | outputs[in2]
                case "XOR":
                    outputs[out] = outputs[in1] ^ outputs[in2]

zs = {k:v for k,v in outputs.items() if k.startswith("z")}
print(zs)
dec = [0]*len(zs)
for wire, val in zs.items():
    dec[int(wire[1:])] = str(val)
dec = reversed(dec)
res = int("".join(dec), 2)
print(f"Solution: {res}\n")
copy(res)
# submit(res)

print(f"----{(time.time()-st):.3f} s----")