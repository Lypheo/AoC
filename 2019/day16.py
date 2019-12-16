from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
import itertools
# import networkx as nx
# import re, sys
# sys.setrecursionlimit(2000)

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def getints(string):

    return [int(x) for x in re.findall(r"[-\d.]+", string)]

def intcode(data=input_data, prog_in=[1]):
    inp = defaultdict(int)
    inp.update({i: v for i,v in enumerate([int(i) for i in data. split(",")])})
    pointer = 0
    rel_base = 0
    op = inp[pointer]
    opcode = op % 100
    modes = [(op % 10**(x+1))//(10**x) for x in reversed(range(2, 5))]
    
    def args(num, pos = False):
        if modes[3-num] == 0:
            return inp[inp[pointer+num]] if not pos else inp[pointer+num]
        elif modes[3-num] == 2:
            return inp[rel_base + inp[pointer+num]] if not pos else rel_base + inp[pointer+num]
        else:
            return inp[pointer+num]

    while opcode != 99:
        if opcode == 1:
            inp[args(3, True)] = args(1) + args(2)
            pointer += 4
        elif opcode == 2:
            inp[args(3, True)] = args(1) * args(2)
            pointer += 4
        elif opcode == 3:
            inp[args(1, True)] = prog_in.pop()
            pointer += 2
        elif opcode == 4:
            yield args(1)
            pointer += 2
        elif opcode == 5:
            pointer = pointer + 3 if args(1) == 0 else args(2)
        elif opcode == 6:
            pointer = pointer + 3 if args(1) != 0 else args(2)
        elif opcode == 7:
            inp[args(3, True)] = 1 if args(1) < args(2) else 0
            pointer += 4
        elif opcode == 8:
            inp[args(3, True)] = 1 if args(1) == args(2) else 0
            pointer += 4
        elif opcode == 9:
            rel_base += args(1)
            pointer += 2

        op = inp[pointer]
        opcode = op % 100
        modes = [(op % 10**(x+1))//(10**x) for x in reversed(range(2, 5))]

    yield "END"

def draw(grid):
    minx = int(min(z.real for z in grid.keys()))
    maxx = int(max(z.real for z in grid.keys()))
    miny = int(min(z.imag for z in grid.keys()))
    maxy = int(max(z.imag for z in grid.keys()))
    for y in reversed(range(miny, maxy+1)):
        for x in range(minx, maxx+1):
            val = grid[complex(x, y)]
            print(val if val != 0 else " ", end="")
        print("\n", end="")
    print("\n\n", end="")

def solve(inp=input_data):
    offset = int(inp[:7])
    inp = inp#*10000
    new = [int(x) for x in inp]
    for i in range(100):
        signal = new
        new = []
        for j, num in enumerate(signal):
            a = [(0,1,0,-1)]*(j+1)
            a = list(zip(*a))
            a = sum(a, ())
            a = itertools.cycle(a)
            next(a)
            sum_ = sum(signal[k] * next(a) for k in range(len(signal)))
            new.append(abs(sum_) % 10 )
        print(i)


    out = "".join(str(i) for i in new[:8])
    return out, None

test1 = "80871224585914546619083218645595"
a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 
