from datetime import datetime
from aocd.models import Puzzle
from aocd import submit


day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def isvalida(i):
    double = 0
    increase = True
    old = str(i)[0]
    for j in str(i)[1:]:
        if j == old:
            double += 1
        if int(j) < int(old):
            increase = False
        old = j

    return True if double > 0 and increase else False

def isvalidb(i):
    double = {}
    increase = True
    old = str(i)[0]
    for j in str(i)[1:]:
        if j == old:
            try:
                double[j] += 1
            except KeyError:
                double[j] = 1

        if int(j) < int(old):
            increase = False
        old = j

    return True if (len(double.values()) != 0 and any(i == 1 for i in double.values())) and increase else False

# print(isvalid(112233))

def solve(inp=input_data):
    rng = [int(x) for x in inp.split("-")]
    counta = 0
    countb = 0
    for i in range(rng[0], rng[1]+1):
        if isvalida(i):
            counta += 1
        if isvalidb(i):
            countb += 1

    return counta, countb

a, b = solve("171309-643603")
print(f"Part 1: {a}")
if b: print(f"Part 2: {b}")
