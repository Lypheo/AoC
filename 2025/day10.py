import os
import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from aocl import *
from functional import seq
from fn import _ as l
from pyperclip import copy
import networkx as nx
from collections import Counter
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

st=time.time()

puzzle = Puzzle(year=2025, day=10)
inp = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()
inp = puzzle.input_data

inp = lines(inp)
machines = []
for line in inp:
    parts = line.split()
    lights = tuple(c == "#" for c in parts[0][1:-1])
    joltage = tuple(ints(parts[-1]))
    buttons = [tuple(ints(btn)) for btn in parts[1:-1]]
    machines.append((lights, buttons, joltage))
res = 0
for lights, buttons, joltage in machines:
    buttons = [[1 if j in btn else 0 for j in range(len(joltage))] for btn in buttons]
    c = [1 for _ in range(len(buttons))]
    A = np.array(buttons).transpose()
    constraints = [LinearConstraint(A, joltage, joltage)]
    sol = milp(c=c, integrality=c, constraints=constraints, bounds=Bounds(lb=np.zeros(len(buttons)), ub=np.full(len(buttons), np.inf)))
    assert sol.success
    res += sol.fun

print(f"Solution: {res}\n")
copy(res)

print(f"----{(time.time()-st):.3f} s----")