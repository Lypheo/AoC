from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def isvalid(i):
    double = defaultdict(int)
    increase = True
    old = str(i)[0]
    for j in str(i)[1:]:
        if j == old:
            double[j] += 1
        if int(j) < int(old):
            increase = False
        old = j

    if not increase:
        return False, False

    a = any(i > 0 for i in double.values()) 
    b = any(i == 1 for i in double.values())
    return a, b

pws = set()
def solve(inp=input_data):
    rng = [int(x) for x in inp.split("-")]
    counta = 0
    countb = 0
    for i in range(rng[0], rng[1]+1):
        if isvalid(i)[0]:
            counta += 1
        if isvalid(i)[1]:
            countb += 1

    return counta, countb

a, b = solve("171309-643603")
print(kag.difference(pws))
print(f"Part 1: {a}")
print(f"Part 2: {b}")
