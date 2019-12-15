from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
import itertools
from collections import defaultdict

day = datetime.today().day
puzzle = Puzzle(year=2019, day=7)
input_data = puzzle.input_data

def intcode(data=input_data, prog_in=[1]):
    inp = defaultdict(int)
    inp.update({i: v for i,v in enumerate([int(i) for i in data.split(",")])})
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

def solve(inp=input_data):
    p1 = lambda num, phase: intcode(inp, [p1(num-1, phase) if num != 0 else 0, phase[num]]).__next__()
    p1_max = max(p1(4, i) for i in itertools.permutations([0,1,2,3,4]))
    signals = []
    for i in  itertools.permutations([5, 6, 7, 8, 9]):
        proginp = [[i[j]] if j != 0 else [0, i[j]] for j in range(5)]
        progs = [intcode(inp, proginp[i]) for i in range(5)]
        while proginp[0][0] != "END":
            signal = proginp[0][0]
            for k in range(5):
                proginp[k+1 if k != 4 else 0].insert(0, next(progs[k]))
        signals.append(signal)
    return p1_max, max(signals)

test = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
a, b = solve()
print(f"Part 1: {a}")
print(f"Part 2: {b}")