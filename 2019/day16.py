from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
import itertools
import numpy as np
# import networkx as nx
# import re, sys
# sys.setrecursionlimit(2000)

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    offset = int(inp[:7])
    # offset = 0
    inp = [int(x) for x in inp]
    x1 = []
    # x2 = inp
    x2 = inp*10000
    for i in range(1,len(x2)+1):
        pattern = np.tile(np.repeat([0,1,0,-1], i), int(len(x2)/ (i*4)) + 1)
        x1.append(pattern[1:len(x2)+1])
        if i % 5000 == 0:
            print(i)

    for i in range(100):
        x2 = abs(np.matmul(x1, x2)) % 10

    out = "".join(str(i)[-1] for i in x2[offset:offset+8])
    return out, None

test1 = "03036732577212944063491565474664"
a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 
